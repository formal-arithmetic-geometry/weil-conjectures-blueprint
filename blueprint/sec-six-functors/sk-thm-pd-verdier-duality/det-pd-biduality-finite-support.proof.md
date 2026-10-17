+++
kind = "proof"
of = "det-pd-biduality-finite-support"
uses = ["lem-weil-verdier-preservation-strata", "lem-fin-coordinate-generic-dimension", "det-pd-generic-dualizing-twist", "lem-weil-delta-restriction"]
+++
*Constructibility.* By [lem-weil-verdier-preservation-strata], $D_XK$ and
$D_XD_XK$ lie in $D^b_{ctf}(X_{\mathrm{\acute et}},A)$, so the cone $\Delta$ is
bounded constructible.

*Nonclosed points.* Let $x\in X$ be nonclosed and choose an affine open
neighbourhood $V$ of $x$. Since $x$ is nonclosed, $\kappa(x)$ has positive
transcendence degree over $k$, so among finitely many algebra generators of
$\Gamma(V,\mathcal O_V)$ there is one, $t$, whose image in $\kappa(x)$ is
transcendental over $k$. The induced map $t\colon V\to\mathbf A^1_k$ sends $x$
to the generic point. Every component of $V$ meeting the generic fibre of $t$
loses one dimension in it ([lem-fin-coordinate-generic-dimension]); algebraic
field extension preserves this bound, so the geometric generic fibre
$V_{\bar\eta}$, $\bar\eta=\operatorname{Spec}\overline{k(t)}$, has dimension at
most $d-1$. By the hypothesis over $\overline{k(t)}$, $\delta_{g^*(K|_V)}$ is an
isomorphism. By [det-pd-generic-dualizing-twist] it is identified with
$g^*\delta_{K|_V}$, and $\delta_{K|_V}=\delta_K|_V$ by
[lem-weil-delta-restriction]. Hence $g^*\Delta|_V=0$. Every geometric point of
$X$ above $x$ factors through $V_{\bar\eta}$ after choosing an algebraic closure
of $k(t)$ in its algebraically closed residue field, so $\Delta$ has zero
geometric stalks above $x$.

*Finiteness.* Each of the finitely many cohomology sheaves of $\Delta$ is
constructible, so its support is a constructible subset, and by the previous
step it contains only closed points. A constructible subset of a Noetherian
finite-type $k$-scheme containing only closed points is finite: in a finite
decomposition into locally closed pieces, a positive-dimensional piece would
contain a nonclosed generic point. Thus all cohomology sheaves of $\Delta$ are
supported on one finite set of closed points.
