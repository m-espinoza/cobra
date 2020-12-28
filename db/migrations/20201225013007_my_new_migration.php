<?php
declare(strict_types=1);

use Phinx\Migration\AbstractMigration;

final class MyNewMigration extends AbstractMigration
{
    /**
     * Change Method.
     *
     * Write your reversible migrations using this method.
     *
     * More information on writing migrations is available here:
     * https://book.cakephp.org/phinx/0/en/migrations.html#the-change-method
     *
     * Remember to call "create()" or "update()" and NOT "save()" when working
     * with the Table class.
     */
    public function change(): void
    {
        $empresa = $this->table('empresa', ['id' => 'id_empresa', 'primary_key' => ['id_empresa']]);
        $empresa->addColumn('empresa', 'string', ['limit' => 50])
            ->create();
        
        $cliente = $this->table('cliente', ['id' => 'id_cliente', 'primary_key' => ['id_cliente']]);
        $cliente->addColumn('cuenta', 'integer')
            ->addColumn('dni', 'integer')
            ->addColumn('nombre', 'string', ['limit' => 140])
            ->addColumn('telefono', 'string' , ['limit' => 13, 'null' => true])
            ->addColumn('direccion', 'string' , ['limit' => 255, 'null' => true])
            ->addColumn('deuda', 'float')
            ->addColumn('id_empresa', 'integer')
            ->addIndex(['id_empresa'])
            ->addForeignKey('id_empresa', 'empresa', 'id_empresa', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->create();        

        $estado = $this->table('estado', ['id' => 'id_estado', 'primary_key' => ['id_estado']]);
        $estado->addColumn('estado', 'string', ['limit' => 50])
            ->create();

        $usuario_permiso = $this->table('usuario_permiso', ['id' => 'id_usuario_permiso', 'primary_key' => ['id_usuario_permiso']]);
        $usuario_permiso->addColumn('permiso', 'string', ['limit' => 50])
            ->addColumn('usuario', 'integer')
            ->addColumn('empresa', 'integer')
            ->addColumn('cliente', 'integer')
            ->addColumn('lista', 'integer')
            ->addColumn('evento', 'integer')
            ->addColumn('informe', 'integer')
            ->create();

        $usuario = $this->table('usuario', ['id' => 'id_usuario', 'primary_key' => ['id_usuario']]);
        $usuario->addColumn('usuario', 'string', ['limit' => 50])
            ->addColumn('contrasena', 'string', ['limit' => 15])
            ->addColumn('id_empresa', 'integer')
            ->addColumn('id_estado', 'integer')
            ->addColumn('id_usuario_permiso', 'integer')
            ->addIndex(['id_empresa', 'id_estado', 'id_usuario_permiso'])
            ->addForeignKey('id_estado', 'estado', 'id_estado', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_empresa', 'empresa', 'id_empresa', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_usuario_permiso', 'usuario_permiso', 'id_usuario_permiso', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->create();

        $mora = $this->table('mora', ['id' => 'id_mora', 'primary_key' => ['id_mora']]);
        $mora->addColumn('mora', 'string', ['limit' => 80])
            ->create();

        $lista = $this->table('lista', ['id' => 'id_lista', 'primary_key' => ['id_lista']]);
        $lista->addColumn('lista', 'string', ['limit' => 140])
            ->addColumn('fecha_creacion', 'date')
            ->addColumn('fecha_fin', 'date')
            ->addColumn('id_empresa', 'integer')
            ->addColumn('id_mora', 'integer')
            ->addColumn('id_estado', 'integer')
            ->addIndex(['id_empresa', 'id_mora', 'id_estado'])
            ->addForeignKey('id_empresa', 'empresa', 'id_empresa', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_mora', 'mora', 'id_mora', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_estado', 'estado', 'id_estado', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->create();

        $lista_cliente = $this->table('lista_cliente', ['id' => 'id_lista_cliente', 'primary_key' => ['id_lista_cliente']]);
        $lista_cliente->addColumn('id_lista', 'integer')
            ->addColumn('id_cliente', 'integer')
            ->addColumn('id_usuario', 'integer')
            ->addIndex(['id_lista', 'id_cliente', 'id_usuario'])
            ->addForeignKey('id_lista', 'lista', 'id_lista', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_cliente', 'cliente', 'id_cliente', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_usuario', 'usuario', 'id_usuario', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->create();

        $evento_tipo = $this->table('evento_tipo', ['id' => 'id_evento_tipo', 'primary_key' => ['id_evento_tipo']]);
        $evento_tipo->addColumn('evento_tipo', 'string', ['limit' => 50])
            ->create();

        $evento_respuesta = $this->table('evento_respuesta', ['id' => 'id_evento_respuesta', 'primary_key' => ['id_evento_respuesta']]);
        $evento_respuesta->addColumn('evento_respuesta', 'string', ['limit' => 50])
            ->create();

        $evento = $this->table('evento', ['id' => 'id_evento', 'primary_key' => ['id_evento']]);
        $evento->addColumn('id_lista_cliente', 'integer')
            ->addColumn('id_evento_tipo', 'integer')
            ->addColumn('id_evento_respuesta', 'integer')
            ->addColumn('mensaje', 'string', ['limit' => 255, 'null' => true])
            ->addColumn('fecha_evento', 'date')
            ->addColumn('fecha_evento_pendiente', 'date', ['null' => true])
            ->addIndex(['id_lista_cliente', 'id_evento_tipo', 'id_evento_respuesta'])
            ->addForeignKey('id_lista_cliente', 'lista_cliente', 'id_lista_cliente', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_evento_tipo', 'evento_tipo', 'id_evento_tipo', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])
            ->addForeignKey('id_evento_respuesta', 'evento_respuesta', 'id_evento_respuesta', ['delete'=> 'NO_ACTION', 'update'=> 'NO_ACTION'])            
            ->create();

    }
}
