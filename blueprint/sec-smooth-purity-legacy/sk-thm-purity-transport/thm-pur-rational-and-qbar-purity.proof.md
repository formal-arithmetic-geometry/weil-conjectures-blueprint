+++
kind  = "proof"
of    = "thm-pur-rational-and-qbar-purity"
+++
Step 1: the $E$-stage. An $E$-object $K$ of
[def-weil-pbc-rational-category] is presented by a lattice
$K_{\mathcal O_E}\in D^b_{ctf}(\cdot,\mathcal O_E)$ with
$K_E=K_{\mathcal O_E}\otimes^L_{\mathcal O_E}E$. The adic purity
isomorphism

$$
\gamma_{f,K_{\mathcal O_E}}:\ Lf^*K_{\mathcal O_E}(d)[2d]
\xrightarrow{\ \sim\ }Rf^!K_{\mathcal O_E}
$$

of [thm-pur-adic-reconstruction] for the lattice, extended along
the exact functor $-\otimes^L_{\mathcal O_E}E$ (exact because
$\mathcal O_E\to E$ is flat), is an isomorphism

$$
\gamma_{f,K_E}:\ Lf^*K_E(d)[2d]\xrightarrow{\ \sim\ }Rf^!K_E
$$

between the $E$-objects, i.e. the $E$-purity isomorphism of
[def-weil-pbc-rational-category]. Step 2: the $\Qlb$-stage.
A $\Qlb$-object of [def-weil-pbc-qbar-category] is represented
by an $E$-object $K_E$ for some finite $E/\Ql$ (no idempotent is
needed, the finite-stage categories being idempotent complete); the
$\Qlb$-purity isomorphism is the transport of the $E$-purity
isomorphism of Step 1 along the scalar extension
$E\hookrightarrow\Qlb$, well defined by the independence of
[prop-pur-rational-purity-transitivity-summands].
