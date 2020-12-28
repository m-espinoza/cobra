<?php


use Phinx\Seed\AbstractSeed;

class UserSeeder extends AbstractSeed
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
        $estados = [
            [
                'estado'  => 'habilitado'
            ],
            [
                'estado'  => 'Deshabilitado'
            ]
        ];

        $estado = $this->table('estado')
            ->insert($estados)
            ->saveData();


        $moras = [
            [
                'mora'  => 'Normal'
            ],
            [
                'mora'  => 'Mora Temprana'
            ],
            [
                'mora'  => 'Mora Intermedia'
            ],
            [
                'mora'  => 'Extrajudicial'
            ]
        ];

        $mora = $this->table('mora')
            ->insert($moras)
            ->saveData();


        $empresas = [
            [
                'empresa'  => 'Prueba S.A'
            ]
        ];

        $empresa = $this->table('empresa')
            ->insert($empresas)
            ->saveData();


        $permisos = [
            [
                'permiso'  => 'Administrador',
                'usuario' => '1',
                'empresa' => '1',
                'cliente' => '1',
                'lista' => '1',
                'evento' => '1',
                'informe' => '1'
            ],
            [
                'permiso'  => 'Call center',
                'usuario' => '0',
                'empresa' => '0',
                'cliente' => '1',
                'lista' => '1',
                'evento' => '1',
                'informe' => '0'
            ],
            [
                'permiso'  => 'Gerente',
                'usuario' => '0',
                'empresa' => '0',
                'cliente' => '0',
                'lista' => '0',
                'evento' => '0',
                'informe' => '1'
            ]
            
        ];

        $usuario_permiso = $this->table('usuario_permiso')
            ->insert($permisos)
            ->saveData();


        $usuarios = [
            [
                'usuario'  => 'Administrador',
                'contrasena'  => '123',
                'id_empresa'  => '1',
                'id_estado'  => '1',
                'id_usuario_permiso'  => '1'
            ],
            [
                'usuario'  => 'Operadora 1',
                'contrasena'  => '123',
                'id_empresa'  => '1',
                'id_estado'  => '1',
                'id_usuario_permiso'  => '2'
            ]
        ];

        $usuario = $this->table('usuario')
            ->insert($usuarios)
            ->saveData();


        $tipos = [
            [
                'evento_tipo'  => 'Llamada'
            ],
            [
                'evento_tipo'  => 'SMS'
            ],
            [
                'evento_tipo'  => 'Whatsapp'
            ],
            [
                'evento_tipo'  => 'Carta'
            ]
        ];

        $evento_tipo = $this->table('evento_tipo')
            ->insert($tipos)
            ->saveData();


        $respuestas = [
            [
                'evento_respuesta'  => 'Contestador'
            ],
            [
                'evento_respuesta'  => 'Atendió titular'
            ],
            [
                'evento_respuesta'  => 'Numero inexistente'
            ]
        ];

        $evento_respuesta = $this->table('evento_respuesta')
            ->insert($respuestas)
            ->saveData();


        $clientes = [
            [
                'cuenta'  => '1',
                'dni'  => '12312312',
                'nombre'  => 'Cliente Prueba',
                'telefono'  => '5492611423456',
                'direccion'  => 'Calle sola 123 - Ciudad - Mendoza',
                'deuda'  => '1000',
                'id_empresa'  => '1'
            ]
            
        ];

        $cliente = $this->table('cliente')
            ->insert($clientes)
            ->saveData();
    }
}
