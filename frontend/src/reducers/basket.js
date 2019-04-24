import * as R from 'ramda';

import {
	ADD_PRODUCT_TO_BASKET,
	REMOVE_PRODUCT_FROM_BASKET, 
	CLEAN_BASKET
} from '../actionTypes'

const initialState = []

export default (state = initialState, {type, payload}) => {
	switch (type) {
		case ADD_PRODUCT_TO_BASKET:
		  return R.append(payload, state)
		case REMOVE_PRODUCT_FROM_BASKET:
		  return R.without(R.of(payload), state)
		case CLEAN_BASKET:
		  return []
		default:
			return state
	}
}