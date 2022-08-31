/** @odoo-module **/    


import { LaunchShopOrderWidget } from '@oshop/widgets/o_shop';
import { action_registry } from 'web.core';

action_registry.add('shop.order.widgets', LaunchShopOrderWidget);
console.log("files loaded");

/**
 * There is a very important point to know: Odoo needs to know which files 
 * should be translated into Odoo modules and which files should not be translated. 
 * This is an opt-in system: Odoo will look at the first line of a JS file and check 
 * if it contains the string `@odoo-module`. If so, it will automatically be converted
 * to an Odoo module.
 */
