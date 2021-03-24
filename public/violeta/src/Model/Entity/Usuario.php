<?php
declare(strict_types=1);

namespace App\Model\Entity;

use Cake\ORM\Entity;

/**
 * Usuario Entity
 *
 * @property int $id_usuario
 * @property string $usuario
 * @property string $email
 * @property string $contrasena
 * @property int $id_empresa
 * @property int $id_estado
 * @property int $id_usuario_permiso
 */
class Usuario extends Entity
{
    /**
     * Fields that can be mass assigned using newEntity() or patchEntity().
     *
     * Note that when '*' is set to true, this allows all unspecified fields to
     * be mass assigned. For security purposes, it is advised to set '*' to false
     * (or remove it), and explicitly make individual fields accessible as needed.
     *
     * @var array
     */
    protected $_accessible = [
        'usuario' => true,
        'email' => true,
        'contrasena' => true,
        'id_empresa' => true,
        'id_estado' => true,
        'id_usuario_permiso' => true,
    ];
}
