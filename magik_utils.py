from comfy_api.latest import ComfyExtension, io

CATEGORY = "Magik/Util"
# Largest integer the JS frontend represents exactly.
JS_SAFE_MAX = 2**53 - 1
SEED_MAX = 0xFFFFFFFFFFFFFFFF


class MagikInt(io.ComfyNode):
    """Integer constant, also emitted as float and text."""

    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="Magik.Int",
            display_name="Magik Int",
            category=CATEGORY,
            inputs=[
                io.Int.Input("value", default=0, min=0, max=JS_SAFE_MAX),
            ],
            outputs=[
                io.Int.Output("int"),
                io.Float.Output("float"),
                io.String.Output("text"),
            ],
        )

    @classmethod
    def execute(cls, value):
        return io.NodeOutput(value, float(value), str(value))


class MagikFloat(io.ComfyNode):
    """Float constant, also emitted as int and text."""

    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="Magik.Float",
            display_name="Magik Float",
            category=CATEGORY,
            inputs=[
                io.Float.Input("value", default=0.0, min=0.0, max=float(JS_SAFE_MAX), step=0.01),
            ],
            outputs=[
                io.Float.Output("float"),
                io.Int.Output("int"),
                io.String.Output("text"),
            ],
        )

    @classmethod
    def execute(cls, value):
        return io.NodeOutput(value, int(value), str(value))


class MagikSeed(io.ComfyNode):
    """Seed constant with native control-after-generate."""

    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="Magik.Seed",
            display_name="Magik Seed",
            category=CATEGORY,
            inputs=[
                io.Int.Input("seed", default=0, min=0, max=SEED_MAX, control_after_generate=True),
            ],
            outputs=[
                io.Int.Output("seed"),
            ],
            is_output_node=True,
        )

    @classmethod
    def execute(cls, seed):
        return io.NodeOutput(seed)


class MagikUtilExtension(ComfyExtension):
    async def get_node_list(self):
        return [MagikInt, MagikFloat, MagikSeed]


async def comfy_entrypoint():
    return MagikUtilExtension()
