<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Estado $estado
 */
?>
<div class="row">
    <aside class="column">
        <div class="side-nav">
            <h4 class="heading"><?= __('Actions') ?></h4>
            <?= $this->Html->link(__('Edit Estado'), ['action' => 'edit', $estado->id_estado], ['class' => 'side-nav-item']) ?>
            <?= $this->Form->postLink(__('Delete Estado'), ['action' => 'delete', $estado->id_estado], ['confirm' => __('Are you sure you want to delete # {0}?', $estado->id_estado), 'class' => 'side-nav-item']) ?>
            <?= $this->Html->link(__('List Estado'), ['action' => 'index'], ['class' => 'side-nav-item']) ?>
            <?= $this->Html->link(__('New Estado'), ['action' => 'add'], ['class' => 'side-nav-item']) ?>
        </div>
    </aside>
    <div class="column-responsive column-80">
        <div class="estado view content">
            <h3><?= h($estado->id_estado) ?></h3>
            <table>
                <tr>
                    <th><?= __('Estado') ?></th>
                    <td><?= h($estado->estado) ?></td>
                </tr>
                <tr>
                    <th><?= __('Id Estado') ?></th>
                    <td><?= $this->Number->format($estado->id_estado) ?></td>
                </tr>
            </table>
        </div>
    </div>
</div>
