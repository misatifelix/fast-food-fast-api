from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from ..models.order_model import order_obj
class FoodListResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str,
    required=True)

    parser.add_argument("price",type=int,
    required=True)

   
    def get(self):
        """"
        Return foods list 
        """
        all_foods = order_obj.get_foods()
        if all_foods:
            return all_foods
        return {"message": "no food items present"}, 404

    @jwt_required
    def post(self):
        """
        Post foods  
        """
        inc_id = order_obj.get_length(order_obj.get_foods()) + 1
        data = FoodListResource.parser.parse_args()
        food_item = order_obj.get_by_name(data['name'],order_obj.get_foods())

        if food_item:
            return {'message': 'food item already added try another'}

        else:
            
            food = {
                'id': inc_id, 'name': data['name'], 'price':data['price']
            }
            order_obj.add_foods(food)
            return food
       

class FoodResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str,
    required=True)

    parser.add_argument("price",type=int,
    required=True)


    def get(self,id):
        """
        Return a specific food item by id
      """
        food = order_obj.get_by_id(id,order_obj.get_foods())
        if food:
            return food, 200
        return {"message": "food item does not exist"}, 404

    #requires a token
    @jwt_required
    def put(self,id):
        """
        Edit the the food item details
        """
        data= FoodResource.parser.parse_args()
        food_to_edit = order_obj.get_by_id(id,order_obj.get_foods())
        if food_to_edit:
            food_to_edit.update(data)
            return food_to_edit,201
        else:
            return {"message":"no item to update"}, 404


    #requires a token
    @jwt_required
    def delete(self,id):
        """
        deelte item
        """
        order_obj.delete_item(id,order_obj.get_foods())
        return {"message":"item has been deleted"}, 202


#admin can alter prices

class ChangePriceResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",type=int,
    required=True)

    #requires a token
    @jwt_required
    def put(self,name):
        data = ChangePriceResource.parser.parse_args()
        food_to_edit = order_obj.get_by_name(name,order_obj.get_foods())
        if food_to_edit:
            food_to_edit.update(data)
            return food_to_edit,201
        else:
            return {"message":"no named item in food list"}, 404
