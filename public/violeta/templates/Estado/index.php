<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Estado[]|\Cake\Collection\CollectionInterface $estado
 */
?>
<div class="estado index content">
    <?= $this->Html->link(__('New Estado'), ['action' => 'add'], ['class' => 'button float-right']) ?>
    <h3><?= __('Estado') ?></h3>
    <div class="table-responsive">
        <table>
            <thead>
                <tr>
                    <th><?= $this->Paginator->sort('id_estado') ?></th>
                    <th><?= $this->Paginator->sort('estado') ?></th>
                    <th class="actions"><?= __('Actions') ?></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($estado as $estado): ?>
                <tr>
                    <td><?= $this->Number->format($estado->id_estado) ?></td>
                    <td><?= h($estado->estado) ?></td>
                    <td class="actions">
                        <?= $this->Html->link(__('View'), ['action' => 'view', $estado->id_estado]) ?>
                        <?= $this->Html->link(__('Edit'), ['action' => 'edit', $estado->id_estado]) ?>
                        <?= $this->Form->postLink(__('Delete'), ['action' => 'delete', $estado->id_estado], ['confirm' => __('Are you sure you want to delete # {0}?', $estado->id_estado)]) ?>
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
