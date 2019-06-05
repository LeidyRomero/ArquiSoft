class SetDefaultClientePuntos < ActiveRecord::Migration[5.2]
  def change
    change_column_default :clientes, :puntos, from: nil, to: 0
  end
end
