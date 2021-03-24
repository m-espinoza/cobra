<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Empresa $empresa
 */
?>
<div class="row">
    <aside class="column">
        <div class="side-nav">
            <h4 class="heading"><?= __('Actions') ?></h4>
            <?= $this->Html->link(__('Edit Empresa'), ['action' => 'edit', $empresa->id_empresa], ['class' => 'side-nav-item']) ?>
            <?= $this->Form->postLink(__('Delete Empresa'), ['action' => 'delete', $empresa->id_empresa], ['confirm' => __('Are you sure you want to delete # {0}?', $empresa->id_empresa), 'class' => 'side-nav-item']) ?>
            <?= $this->Html->link(__('List Empresa'), ['action' => 'index'], ['class' => 'side-nav-item']) ?>
            <?= $this->Html->link(__('New Empresa'), ['action' => 'add'], ['class' => 'side-nav-item']) ?>
        </div>
    </aside>
    <div class="column-responsive column-80">
        <div class="empresa view content">
            <h3><?= h($empresa->id_empresa) ?></h3>
            <table>
                <tr>
                    <th><?= __('Empresa') ?></th>
                    <td><?= h($empresa->empresa) ?></td>
                </tr>
                <tr>
                    <th><?= __('Id Empresa') ?></th>
                    <td><?= $this->Number->format($empresa->id_empresa) ?></td>
                </tr>
            </table>
        </div>
    </div>
</div>
