<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Usuario[]|\Cake\Collection\CollectionInterface $usuario
 */
?>
<div class="usuario index content">
    <?= $this->Html->link(__('New Usuario'), ['action' => 'add'], ['class' => 'button float-right']) ?>
    <h3><?= __('Usuario') ?></h3>
    <div class="table-responsive">
        <table>
            <thead>
                <tr>
                    <th><?= $this->Paginator->sort('id_usuario') ?></th>
                    <th><?= $this->Paginator->sort('usuario') ?></th>
                    <th><?= $this->Paginator->sort('email') ?></th>
                    <th><?= $this->Paginator->sort('contrasena') ?></th>
                    <th><?= $this->Paginator->sort('id_empresa') ?></th>
                    <th><?= $this->Paginator->sort('id_estado') ?></th>
                    <th><?= $this->Paginator->sort('id_usuario_permiso') ?></th>
                    <th class="actions"><?= __('Actions') ?></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($usuario as $usuario): ?>
                <tr>
                    <td><?= $this->Number->format($usuario->id_usuario) ?></td>
                    <td><?= h($usuario->usuario) ?></td>
                    <td><?= h($usuario->email) ?></td>
                    <td><?= h($usuario->contrasena) ?></td>
                    <td><?= $this->Number->format($usuario->id_empresa) ?></td>
                    <td><?= $this->Number->format($usuario->id_estado) ?></td>
                    <td><?= $this->Number->format($usuario->id_usuario_permiso) ?></td>
                    <td class="actions">
                        <?= $this->Html->link(__('View'), ['action' => 'view', $usuario->id_usuario]) ?>
                        <?= $this->Html->link(__('Edit'), ['action' => 'edit', $usuario->id_usuario]) ?>
                        <?= $this->Form->postLink(__('Delete'), ['action' => 'delete', $usuario->id_usuario], ['confirm' => __('Are you sure you want to delete # {0}?', $usuario->id_usuario)]) ?>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <div class="paginator">
        <ul class="pagination">
            <?= $this->Paginator->first('<< ' . __('first')) ?>
            <?= $this->Paginator->prev('< ' . __('previous')) ?>
            <?= $this->Paginator->numbers() ?>
            <?= $this->Paginator->next(__('next') . ' >') ?>
            <?= $this->Paginator->last(__('last') . ' >>') ?>
        </ul>
        <p><?= $this->Paginator->counter(__('Page {{page}} of {{pages}}, showing {{current}} record(s) out of {{count}} total')) ?></p>
    </div>
</div>
