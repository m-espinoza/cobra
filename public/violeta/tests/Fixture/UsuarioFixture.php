<?php
declare(strict_types=1);

namespace App\Test\Fixture;

use Cake\TestSuite\Fixture\TestFixture;

/**
 * UsuarioFixture
 */
class UsuarioFixture extends TestFixture
{
    /**
     * Table name
     *
     * @var string
     */
    public $table = 'usuario';
    /**
     * Fields
     *
     * @var array
     */
    // phpcs:disable
    public $fields = [
        'id_usuario' => ['type' => 'integer', 'length' => null, 'unsigned' => false, 'null' => false, 'default' => null, 'comment' => '', 'autoIncrement' => true, 'precision' => null],
        'usuario' => ['type' => 'string', 'length' => 50, 'null' => false, 'default' => null, 'collate' => 'utf8_general_ci', 'comment' => '', 'precision' => null],
        'email' => ['type' => 'string', 'length' => 140, 'null' => false, 'default' => null, 'collate' => 'utf8_general_ci', 'comment' => '', 'precision' => null],
        'contrasena' => ['type' => 'string', 'length' => 15, 'null' => false, 'default' => null, 'collate' => 'utf8_general_ci', 'comment' => '', 'precision' => null],
        'id_empresa' => ['type' => 'integer', 'length' => null, 'unsigned' => false, 'null' => false, 'default' => null, 'comment' => '', 'precision' => null, 'autoIncrement' => null],
        'id_estado' => ['type' => 'integer', 'length' => null, 'unsigned' => false, 'null' => false, 'default' => null, 'comment' => '', 'precision' => null, 'autoIncrement' => null],
        'id_usuario_permiso' => ['type' => 'integer', 'length' => null, 'unsigned' => false, 'null' => false, 'default' => null, 'comment' => '', 'precision' => null, 'autoIncrement' => null],
        '_indexes' => [
            'id_empresa' => ['type' => 'index', 'columns' => ['id_empresa', 'id_estado', 'id_usuario_permiso'], 'length' => []],
            'id_estado' => ['type' => 'index', 'columns' => ['id_estado'], 'length' => []],
            'id_usuario_permiso' => ['type' => 'index', 'columns' => ['id_usuario_permiso'], 'length' => []],
        ],
        '_constraints' => [
            'primary' => ['type' => 'primary', 'columns' => ['id_usuario'], 'length' => []],
            'usuario_ibfk_3' => ['type' => 'foreign', 'columns' => ['id_usuario_permiso'], 'references' => ['usuario_permiso', 'id_usuario_permiso'], 'update' => 'noAction', 'delete' => 'noAction', 'length' => []],
            'usuario_ibfk_2' => ['type' => 'foreign', 'columns' => ['id_empresa'], 'references' => ['empresa', 'id_empresa'], 'update' => 'noAction', 'delete' => 'noAction', 'length' => []],
            'usuario_ibfk_1' => ['type' => 'foreign', 'columns' => ['id_estado'], 'references' => ['estado', 'id_estado'], 'update' => 'noAction', 'delete' => 'noAction', 'length' => []],
        ],
        '_options' => [
            'engine' => 'InnoDB',
            'collation' => 'utf8_general_ci'
        ],
    ];
    // phpcs:enable
    /**
     * Init method
     *
     * @return void
     */
    public function init(): void
    {
        $this->records = [
            [
                'id_usuario' => 1,
                'usuario' => 'Lorem ipsum dolor sit amet',
                'email' => 'Lorem ipsum dolor sit amet',
                'contrasena' => 'Lorem ipsum d',
                'id_empresa' => 1,
                'id_estado' => 1,
                'id_usuario_permiso' => 1,
            ],
        ];
        parent::init();
    }
}
