
/** @odoo-module **/

import { Shop } from "../src/widgets/shop";
import { MockServer } from "@web/../tests/helpers/mock_server";
import { makeTestEnv } from "@web/../tests/helpers/mock_env";
import { getFixture } from "@web/../tests/helpers/utils";

const { Component, core, hooks, mount, tags } = owl;

QUnit.module(
    "lunch_order > lunch order links",
    {
        beforeEach: function () {
            this.serverData = {};
            this.serverData.products = {
                'id': 1,
                'name': 'Pizza'
            };
        },
    },
    () => {

        QUnit.test("Shop rendering", async function (assert) {
            const mockRPC = (route, args) => {
                if (route.includes("search")) {
                    assert.step("search product");
                }
            };
            const mockServer = new MockServer(this.serverData, { debug: QUnit.config.debug });
            const env = await makeTestEnv();
            const target = getFixture();
            parent = await mount(Shop, { env, target, props: {} });
        });
    }
);