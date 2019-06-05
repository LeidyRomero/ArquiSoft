class CreateClientes < ActiveRecord::Migration[5.2]
  def change
    create_table :clientes,
    {
      :id           => false,
      :primary_key  => :identificacion
    } do |t|
      t.string :nombre
      t.string :identificacion
      t.integer :puntos
      t.string :email

      t.timestamps
    end
  end
end
