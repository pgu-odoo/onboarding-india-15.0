/** @odoo-module **/

import { MediOrderWidget } from '@medi_zone/widgets/shop';

import { action_registry } from 'web.core';

action_registry.add('medi.order.widgets',MediOrderWidget);