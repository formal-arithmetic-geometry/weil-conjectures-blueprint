+++
id = "det-pd-generic-dualizing-twist"
kind = "lemma"
title = "The dualizing complex and the double dual on a geometric generic fibre"
order = 3431
uses = ["det-pd-generic-direct-image", "det-pd-generic-closed-hom", "lem-weil-duality-pairing", "thm-amb-etale-exceptional-adjoint"]
+++
In the setting of [det-pd-generic-direct-image] take $B=\mathbf A^1_k$, so
$\bar\eta=\operatorname{Spec}\overline{k(t)}$, and let $X$ be a separated
finite-type $\mathbf A^1_k$-scheme. Let $\omega_X=Ra_X^!A$ and
$\omega_{X_{\bar\eta}}=Ra_{X_{\bar\eta}}^!A$ be the dualizing complexes
([thm-amb-etale-exceptional-adjoint]) and $\delta$ the double-dual morphism
of [lem-weil-duality-pairing]. Then, Zariski locally on $X$,

$$
g_X^*\omega_X\simeq\omega_{X_{\bar\eta}}(1)[2],
$$

and for every $K\in D^b_{ctf}(X_{\mathrm{\acute et}},A)$ the internal-Hom
comparison of [det-pd-generic-closed-hom], applied twice, identifies
$g_X^*\delta_K$ with $\delta_{g_X^*K}$.
