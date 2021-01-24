<?php
// in src/Model/Table/ArticlesTable.php
namespace App\Model\Table;

use Cake\ORM\Table;
// the Text class
use Cake\Utility\Text;
// the EventInterface class
use Cake\Event\EventInterface;

use Cake\Validation\Validator;

class ArticlesTable extends Table
{
    public function initialize(array $config): void
    {
        $this->addBehavior('Timestamp');
    }

	public function beforeSave(EventInterface $event, $entity, $options)
	{
	    if ($entity->isNew() && !$entity->slug) {
	        $sluggedTitle = Text::slug($entity->title);
	        // trim slug to maximum length defined in schema
	        $entity->slug = substr($sluggedTitle, 0, 191);
	    }
	}

	public function edit($slug)
	{
	    $article = $this->Articles
	        ->findBySlug($slug)
	        ->firstOrFail();

	    if ($this->request->is(['post', 'put'])) {
	        $this->Articles->patchEntity($article, $this->request->getData());
	        if ($this->Articles->save($article)) {
	            $this->Flash->success(__('Your article has been updated.'));
	            return $this->redirect(['action' => 'index']);
	        }
	        $this->Flash->error(__('Unable to update your article.'));
	    }

	    $this->set('article', $article);
	}	

	public function validationDefault(Validator $validator): Validator
	{
	    $validator
	        ->notEmptyString('title')
	        ->minLength('title', 2)
	        ->maxLength('title', 255)

	        ->notEmptyString('body')
	        ->minLength('body', 2);

	    return $validator;
	}	

	
}

?>