<?php
declare(strict_types=1);

namespace App\Test\TestCase\Model\Table;

use App\Model\Table\EstadoTable;
use Cake\TestSuite\TestCase;

/**
 * App\Model\Table\EstadoTable Test Case
 */
class EstadoTableTest extends TestCase
{
    /**
     * Test subject
     *
     * @var \App\Model\Table\EstadoTable
     */
    protected $Estado;

    /**
     * Fixtures
     *
     * @var array
     */
    protected $fixtures = [
        'app.Estado',
    ];

    /**
     * setUp method
     *
     * @return void
     */
    public function setUp(): void
    {
        parent::setUp();
        $config = $this->getTableLocator()->exists('Estado') ? [] : ['className' => EstadoTable::class];
        $this->Estado = $this->getTableLocator()->get('Estado', $config);
    }

    /**
     * tearDown method
     *
     * @return void
     */
    public function tearDown(): void
    {
        unset($this->Estado);

        parent::tearDown();
    }

    /**
     * Test validationDefault method
     *
     * @return void
     */
    public function testValidationDefault(): void
    {
        $this->markTestIncomplete('Not implemented yet.');
    }
}
