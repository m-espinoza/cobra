<?php


use Phinx\Seed\AbstractSeed;

class UsuarioEmail extends AbstractSeed
{
    /**
     * Run Method.
     *
     * Write your database seeder using this method.
     *
     * More information on writing seeders is available here:
     * https://book.cakephp.org/phinx/0/en/seeding.html
     */
    public function run()
    {
        $usuarios = [
            [
                'usuario'  => 'Administrador',
                'email' => 'admin@violeta.com',
                'contrasena'  => '123',
                'id_empresa'  => '1',
                'id_estado'  => '1',
                'id_usuario_permiso'  => '1'
                
            ],
            [
                'usuario'  => 'Operadora 1',
                'email' => 'ope1@violeta.com',
                'contrasena'  => '123',
                'id_empresa'  => '1',
                'id_estado'  => '1',
                'id_usuario_permiso'  => '2'
                
            ]
        ];

        $usuario = $this->table('usuario')
            ->insert($usuarios)
            ->saveData();
    }
}
