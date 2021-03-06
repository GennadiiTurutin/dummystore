import * as R from 'ramda';

import {
	FETCH_PRODUCTS_SUCCESS,
  FETCH_PRODUCT_BY_ID_SUCCESS,
  LIKE_PRODUCT_SUCCESS
} from '../actionTypes'

const initialState = {}

export default (state = initialState, {type, payload}) => {
	switch (type){
	  case FETCH_PRODUCTS_SUCCESS:
      const newValues = R.indexBy(R.prop('id'), payload)
      return R.merge(state, newValues)  
    case LIKE_PRODUCT_SUCCESS:
      return R.merge(state, newValues)               
    case FETCH_PRODUCT_BY_ID_SUCCESS:
      return R.assoc(payload.id, payload, state)
    default:
      return state
	}
}