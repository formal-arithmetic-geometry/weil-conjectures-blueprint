+++
kind = "proof"
of = "det-nearby-kunneth-proper"
uses = ["det-sp-nearby-cycles-exchanges", "lem-trf-ordinary-kunneth"]
+++
Expand both product maps as the tensor maps of $R\bar j_*$, that is, as the maps adjoint to the
tensor products of the counits $\bar j^*R\bar j_*\to1$. The proper exchange of
[det-sp-nearby-cycles-exchanges] is built from proper base change and the composition
identification $R\bar f_*R\bar j_{X*}=R\bar j_{X_1*}Rf_{\bar\eta*}$, so it commutes proper direct
image past those generic open maps. Now take the adjoints of the ordinary Künneth arrows of
[lem-trf-ordinary-kunneth] on the generic fibres. On both sides the adjoint is

$$
f_\eta^*Rf_{\eta*}L\boxtimes g_\eta^*Rg_{\eta*}M\longrightarrow L\boxtimes M,
$$

the tensor product of the two counits. The triangle identities of the adjunctions and their
composition law therefore identify the maps themselves, before and hence after restriction to the
special fibre.
