+++
id = "lem-mg-degree-component-functoriality"
kind = "lemma"
title = "Degree components under subquotients and tensor constructions"
order = 2864
uses = ["def-wf-degree-components", "def-wf-monodromy-data", "lem-wf-arith-extension-group", "lem-wf-stabilizer-density"]
+++
Let $\rho:W(X_0)\to\operatorname{GL}(V)$ have the monodromy data of
[def-wf-monodromy-data]. Let each $Q_i$ be a Weil-stable
subquotient $U_i/U'_i$ of $V$, or an iterated subquotient of one of
the constructions below, and let $Q$ be one of

$$
Q_i,\qquad Q_1\otimes\cdots\otimes Q_a,
\qquad \bigwedge\nolimits^b Q_i.
$$

The closed-stabilizer fact of [lem-wf-stabilizer-density] makes the
induced action algebraic. The action on $Q$ induces a homomorphism

$$
\Phi_Q:G_{\mathrm{arith}}(\rho)\longrightarrow
G_{\mathrm{arith}}(\rho_Q)
$$

which is regular on every degree component, preserves the degree, and has
Zariski-dense image on every degree component. In particular, the image
of a central element is central.
