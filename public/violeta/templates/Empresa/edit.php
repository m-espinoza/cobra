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
            <?= $this->Form->postLink(
                __('Delete'),
                ['action' => 'delete', $empresa->id_empresa],
                ['confirm' => __('Are you sure you want to delete # {0}?', $empresa->id_empresa), 'class' => 'side-nav-item']
            ) ?>
            <?= $this->Html->link(__('List Empresa'), ['action' => 'index'], ['class' => 'side-nav-item']) ?>
        </div>
    </aside>
    <div class="column-responsive column-80">
        <div class="empresa form content">
            <?= $this->Form->create($empresa) ?>
            <fieldset>
                <legend><?= __('Edit Empresa') ?></legend>
                <?php
                    echo $this->Form->control('empresa');
                ?>
            </fieldset>
            <?= $this->Form->button(__('Submit')) ?>
            <?= $this->Form->end() ?>
        </div>
    </div>
</div>
