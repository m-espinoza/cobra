<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Empresa[]|\Cake\Collection\CollectionInterface $empresa
 */
?>
<div class="empresa index content">
    <?= $this->Html->link(__('New Empresa'), ['action' => 'add'], ['class' => 'button float-right']) ?>
    <h3><?= __('Empresa') ?></h3>
    <div class="table-responsive">
        <table>
            <thead>
                <tr>
                    <th><?= $this->Paginator->sort('id_empresa') ?></th>
                    <th><?= $this->Paginator->sort('empresa') ?></th>
                    <th class="actions"><?= __('Actions') ?></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($empresa as $empresa): ?>
                <tr>
                    <td><?= $this->Number->format($empresa->id_empresa) ?></td>
                    <td><?= h($empresa->empresa) ?></td>
                    <td class="actions">
                        <?= $this->Html->link(__('View'), ['action' => 'view', $empresa->id_empresa]) ?>
                        <?= $this->Html->link(__('Edit'), ['action' => 'edit', $empresa->id_empresa]) ?>
                        <?= $this->Form->postLink(__('Delete'), ['action' => 'delete', $empresa->id_empresa], ['confirm' => __('Are you sure you want to delete # {0}?', $empresa->id_empresa)]) ?>
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
