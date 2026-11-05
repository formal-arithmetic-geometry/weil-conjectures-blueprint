+++
id = "lemma-lattices-lisse-e-sheaves--1"
kind = "lemma"
title = "A locally constant sheaf of lattice classes"
name_showing = false
order = 260001
aliases = ["bp-r077-1"]
lean = ["AlgebraicGeometry.ProEtale.exists_lisse_lattice_class_sheaf"]
uses = ["definition-small-pro-etale-site", "definition-lisse-sheaves", "definition-lattice", "lemma-comparison-completed-coefficients"]
+++
The representability assertion is bypassed by the Lean route, which uses the
following statement about a sheaf of lattice classes.

Let $E/\mathbf Q_\ell$ be finite, let $X$ be a scheme, and let $L$ be an
$E_X$-module on $X_{\mathrm{pro}\acute{e}t}$ which is locally free of finite rank.
There is a locally constant sheaf of sets $F$ on $X_{\mathrm{pro}\acute{e}t}$
and a pro-étale covering $\{U_i\to X\}$ such that $F(U_i)$ is nonempty for every
$i$. For every object $U$ with $F(U)$ nonempty, there is a locally free
$\mathcal O_{E,X}|_U$-module $M$ of finite rank on the slice site
$X_{\mathrm{pro}\acute{e}t}/U$, together with an isomorphism

$$
M\otimes_{\mathcal O_{E,X}|_U}E_X|_U\simeq L|_U.
$$

The ranks may vary, and rank zero and the empty scheme are allowed.
