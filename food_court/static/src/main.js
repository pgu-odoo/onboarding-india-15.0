/** @odoo-module **/

import { LunchOrderWidget } from '@food_court/widgets/shop';
import { action_registry } from 'web.core';

action_registry.add('lunch.order.widgets', LunchOrderWidget);
