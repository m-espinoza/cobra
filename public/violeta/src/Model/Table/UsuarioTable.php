<?php
declare(strict_types=1);

namespace App\Model\Table;

use Cake\ORM\Query;
use Cake\ORM\RulesChecker;
use Cake\ORM\Table;
use Cake\Validation\Validator;

/**
 * Usuario Model
 *
 * @method \App\Model\Entity\Usuario newEmptyEntity()
 * @method \App\Model\Entity\Usuario newEntity(array $data, array $options = [])
 * @method \App\Model\Entity\Usuario[] newEntities(array $data, array $options = [])
 * @method \App\Model\Entity\Usuario get($primaryKey, $options = [])
 * @method \App\Model\Entity\Usuario findOrCreate($search, ?callable $callback = null, $options = [])
 * @method \App\Model\Entity\Usuario patchEntity(\Cake\Datasource\EntityInterface $entity, array $data, array $options = [])
 * @method \App\Model\Entity\Usuario[] patchEntities(iterable $entities, array $data, array $options = [])
 * @method \App\Model\Entity\Usuario|false save(\Cake\Datasource\EntityInterface $entity, $options = [])
 * @method \App\Model\Entity\Usuario saveOrFail(\Cake\Datasource\EntityInterface $entity, $options = [])
 * @method \App\Model\Entity\Usuario[]|\Cake\Datasource\ResultSetInterface|false saveMany(iterable $entities, $options = [])
 * @method \App\Model\Entity\Usuario[]|\Cake\Datasource\ResultSetInterface saveManyOrFail(iterable $entities, $options = [])
 * @method \App\Model\Entity\Usuario[]|\Cake\Datasource\ResultSetInterface|false deleteMany(iterable $entities, $options = [])
 * @method \App\Model\Entity\Usuario[]|\Cake\Datasource\ResultSetInterface deleteManyOrFail(iterable $entities, $options = [])
 */
class UsuarioTable extends Table
{
    /**
     * Initialize method
     *
     * @param array $config The configuration for the Table.
     * @return void
     */
    public function initialize(array $config): void
    {
        parent::initialize($config);

        $this->setTable('usuario');
        $this->setDisplayField('id_usuario');
        $this->setPrimaryKey('id_usuario');
        #$this->belongsTo('Empresa');

        /*$this->belongsTo('Empresa', [
                'className' => 'Empresa'
            ])
            ->setForeignKey('id_empresa')
            ->setProperty('empresa');*/

        $this->belongsTo('Empresa', [
                'className' => 'Empresa',
                'joinTable' => 'Empresa',
                'dependent' => true
            ]);

    }

    /**
     * Default validation rules.
     *
     * @param \Cake\Validation\Validator $validator Validator instance.
     * @return \Cake\Validation\Validator
     */
    public function validationDefault(Validator $validator): Validator
    {
        $validator
            ->integer('id_usuario')
            ->allowEmptyString('id_usuario', null, 'create');

        $validator
            ->scalar('usuario')
            ->maxLength('usuario', 50)
            ->requirePresence('usuario', 'create')
            ->notEmptyString('usuario');

        $validator
            ->email('email')
            ->requirePresence('email', 'create')
            ->notEmptyString('email');

        $validator
            ->scalar('contrasena')
            ->maxLength('contrasena', 15)
            ->requirePresence('contrasena', 'create')
            ->notEmptyString('contrasena');

        $validator
            ->integer('id_empresa')
            ->requirePresence('id_empresa', 'create')
            ->notEmptyString('id_empresa');

        $validator
            ->integer('id_estado')
            ->requirePresence('id_estado', 'create')
            ->notEmptyString('id_estado');

        $validator
            ->integer('id_usuario_permiso')
            ->requirePresence('id_usuario_permiso', 'create')
            ->notEmptyString('id_usuario_permiso');

        return $validator;
    }
}
