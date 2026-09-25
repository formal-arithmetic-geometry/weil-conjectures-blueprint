+++
id = "thm-trf-integral-adic-trace-formula"
kind = "theorem"
title = "Integral adic trace formula"
order = 2563
uses = ["def-trf-adic-system", "def-trf-coefficient-conventions", "def-weil-finite-field-fiber", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "prop-trf-levelwise-compact-support", "prop-trf-trace-formal-laws", "thm-trf-finite-coefficient-map", "thm-trf-grothendieck-lefschetz-finite-ring"]
+++
Fix the global finite-field datum
and the coefficient
conventions, and let
$K_\bullet\in\mathcal D^b_{ctf,\mathrm W,adic}(X,\mathcal O_E)$ with
realization $K_{\mathcal O_E}$. At every finite level assume the
hypotheses, including explicit etale-origin witnesses and
compactification admissibility, and the trace inputs of
[thm-trf-grothendieck-lefschetz-finite-ring].
For every integer $m\geq1$,

$$
\operatorname{tr}_{\mathcal O_E}
\bigl(F_{c,K_\bullet}^m\mid R\Gamma_c(X,K_{\mathcal O_E})\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}
\bigl(F_{y,m}\mid K_{\mathcal O_E,\bar y}\bigr)
$$

in $\mathcal O_E$, where the traces are those of the realized
endomorphisms. Equivalently, the compatible system of the
$A_n$-valued trace formulas of
[thm-trf-grothendieck-lefschetz-finite-ring] for the levels
$K_n$ assembles, in the
adic coefficient datum,
to this identity over $\mathcal O_E$.

## Proof

*Step 1: the realized trace is the compatible system of levelwise
traces.* By [def-weil-pbc-adic-coefficient-datum] the
coefficient ring of the realized category is
$\mathcal O_E=\varprojlim_nA_{E,n}$ (the $\varpi_E$-adic
completion), and by the realization isomorphisms of
[prop-trf-levelwise-compact-support]

$$
P_{\mathcal O_E}=R\Gamma_c(X,K_{\mathcal O_E}),\qquad
P_{\bar y,\mathcal O_E}=(K_{\mathcal O_E})_{\bar y}
$$

are the derived-complete perfect complexes over $\mathcal O_E$ whose
reductions are $P_n=R\Gamma_c(X,K_n)$ and $P_{\bar y,n}=(K_n)_{\bar y}$
(the normalizedness of the system, [def-trf-adic-system], gives
$P_{\mathcal O_E}\otimes^L_{\mathcal O_E}A_n\cong P_n$ and likewise
for the stalks). The categorical trace of an endomorphism of such a
realized perfect complex is therefore the compatible system of the
levelwise traces: by the scalar-extension law of
[thm-trf-finite-coefficient-map] (item (3) of
[prop-trf-trace-formal-laws], the ring homomorphisms
$A_{n+1}\to A_n$ being the coefficient reductions), the elements

$$
\operatorname{tr}_{A_n}\bigl(v_n\mid P_n\bigr)\in A_n
$$

form a compatible system under the transition maps for any endomorphism
$v$ of $P_{\mathcal O_E}$ with reductions $v_n$, hence define the
element

$$
\operatorname{tr}_{\mathcal O_E}(v\mid P_{\mathcal O_E})
=\bigl(\operatorname{tr}_{A_n}(v_n\mid P_n)\bigr)_n\in
\varprojlim_nA_n=\mathcal O_E.
$$

This is the classical levelwise definition of the completed trace (no
non-classical limit machinery is used; the compatibility is the datum
of [thm-trf-finite-coefficient-map], and the finiteness of the
underlying complexes of finite projective modules at each level makes
each trace an element of the finite ring $A_n$, so the compatible
system is an element of the inverse limit).

*Step 2: the levelwise identity is compatible.* By
[prop-trf-levelwise-compact-support] the global and local
Frobenius operators form compatible systems, so the identities

$$
\operatorname{tr}_{A_n}\bigl(F_{c,K_n}^m\mid R\Gamma_c(X,K_n)\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{A_n}\bigl(F_{y,m,n}\mid K_{n,\bar y}\bigr)
$$

of [thm-trf-grothendieck-lefschetz-finite-ring] hold at every
level $n$, and both sides are compatible under the transition maps:
the left-hand side by the scalar-extension law of the categorical trace
of [thm-trf-finite-coefficient-map] applied to the compatible
Frobenius systems, and the right-hand side termwise by the same law
applied to the compatible stalk systems (the set
$X_0(\mathbf F_{q^m})$ over which the sum is taken is the same at
every level, and it is finite, so the sums commute with the
restriction of scalars).

*Step 3: passing to the limit.* The two sides of the levelwise
identities are therefore equal elements of the compatible systems, and
by Step 1 the corresponding realized traces in
$\mathcal O_E=\varprojlim_nA_n$ are those systems; this is the
displayed identity over $\mathcal O_E$, and the derived inverse limit
[def-weil-pbc-derived-inverse-limit] over the point is the
realization functor, so no further computation is needed.
