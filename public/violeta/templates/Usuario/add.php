<?php
/**
 * @var \App\View\AppView $this
 * @var \App\Model\Entity\Usuario $usuario
 */
?>
<div class="row">
    <aside class="column">
        <div class="side-nav">
            <h4 class="heading"><?= __('Actions') ?></h4>
            <?= $this->Html->link(__('List Usuario'), ['action' => 'index'], ['class' => 'side-nav-item']) ?>
        </div>
    </aside>
    <div class="column-responsive column-80">
        <div class="usuario form content">
            <?= $this->Form->create($usuario) ?>
            <fieldset>
                <legend><?= __('Add Usuario') ?></legend>
                <?php
                    echo $this->Form->control('usuario');
                    echo $this->Form->control('email');
                    echo $this->Form->control('contrasena');
                    #echo $this->Form->control('id_empresa');
                    echo $this->Form->control('id_empresa', ['options' => $empresa]);
                    echo $this->Form->control('id_estado');
                    echo $this->Form->control('id_usuario_permiso');
                    
                ?>
            </fieldset>
            <?= $this->Form->button(__('Submit')) ?>
            <?= $this->Form->end()?>

        </div>
    </div>
</div>
