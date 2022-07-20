
/** @odoo-module **/

odoo.define('food_court/static/tests/food_court_tests', function (require) {
    "use strict";

    const ControlPanel = require('web.ControlPanel');
    const testUtils = require("web.test_utils");
    const { patch, unpatch } = require("web.utils");
    const { createWebClient, doAction } = require('@web/../tests/webclient/helpers');
    const { legacyExtraNextTick } = require("@web/../tests/helpers/utils");

    const { dom } = testUtils;

    QUnit.module('Food court', {
        beforeEach: function () {
            this.models = {
                lunch_order: {
                    fields: {
                        name: {string: "Name", type: "char"},
                        state: {string: "State", type: "char"},
                        date_order: {string: "Ordered Date", type: "char"},
                        order_lines: {string: "Ordered Date", type: "One2many"},
                    },
                    records: [
                        {id: 1, display_name: "Genda Swami"},
                    ],
                }
            };
            this.actions = {
                21: {
                    id: 21,
                    name: "Lunch Order",
                    tag: 'lunch.order.widgets',
                    type: 'ir.actions.client',
                }
            };
            this.mockRPC = function (route) {
                if (route === '/web/dataset/call_kw/account.report/get_report_informations') {
                    return Promise.resolve({
                        options: {},
                        buttons: [],
                        main_html: '<a action="go_to_details">Go to detail view</a>',
                    });
                } else if (route === '/web/dataset/call_kw/account.report/go_to_details') {
                    return Promise.resolve({
                        type: "ir.actions.act_window",
                        res_id: 1,
                        res_model: "partner",
                        views: [
                            [false, "form"],
                        ],
                    });
                } else if (route === '/web/dataset/call_kw/account.report/get_html_footnotes') {
                    return Promise.resolve("");
                }
            }
        }
    }, () => {
        QUnit.test("mounted is called once when returning on 'Account Reports' from breadcrumb", async function(assert) {
            // This test can be removed as soon as we don't mix legacy and owl layers anymore.
            assert.expect(7);

            let mountCount = 0;

            patch(ControlPanel.prototype, 'test.ControlPanel', {
                mounted() {
                    mountCount = mountCount + 1;
                    this.__uniqueId = mountCount;
                    assert.step(`mounted ${this.__uniqueId}`);
                    this.__superMounted = this._super.bind(this);
                    this.__superMounted(...arguments);
                },
                willUnmount() {
                    assert.step(`willUnmount ${this.__uniqueId}`);
                    this.__superMounted(...arguments);
                }
            });

            const serverData = {models: this.models, views: this.views, actions: this.actions};
            const webClient = await createWebClient({
                serverData,
                mockRPC: this.mockRPC,
            });

            // await doAction(webClient, 42);
            // await dom.click($(webClient.el).find('a[action="go_to_details"]'));
            // await legacyExtraNextTick();
            // await dom.click($(webClient.el).find('.breadcrumb-item:first'));
            // await legacyExtraNextTick();
            // webClient.destroy();

            // assert.verifySteps([
            //     'mounted 1',
            //     'willUnmount 1',
            //     'mounted 2',
            //     'willUnmount 2',
            //     'mounted 3',
            //     'willUnmount 3',
            // ]);

            unpatch(ControlPanel.prototype, 'test.ControlPanel');
        });

    });

});


// import { Shop } from "../src/widgets/shop";
// import { MockServer } from "@web/../tests/helpers/mock_server";
// import { makeTestEnv } from "@web/../tests/helpers/mock_env";
// import { getFixture } from "@web/../tests/helpers/utils";

// const { Component, core, hooks, mount, tags } = owl;

// QUnit.module(
//     "lunch_order > lunch order links",
//     {
//         beforeEach: function () {
//             this.serverData = {};
//             this.serverData.products = {
//                 'id': 1,
//                 'name': 'Pizza'
//             };
//         },
//     },
//     () => {

//         QUnit.test("Shop rendering", async function (assert) {
//             const mockRPC = (route, args) => {
//                 if (route.includes("search")) {
//                     assert.step("search product");
//                 }
//             };
//             const mockServer = new MockServer(this.serverData, { debug: QUnit.config.debug });
//             const env = await makeTestEnv();
//             const target = getFixture();
//             parent = await mount(Shop, { env, target, props: {} });
//         });
//     }
// );