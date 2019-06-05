class Cliente < ApplicationRecord
    self.primary_key = 'identificacion'
    validates :nombre, presence: true
    validates_format_of :email,:with => /\A[^@\s]+@([^@\s]+\.)+[^@\s]+\z/
end
