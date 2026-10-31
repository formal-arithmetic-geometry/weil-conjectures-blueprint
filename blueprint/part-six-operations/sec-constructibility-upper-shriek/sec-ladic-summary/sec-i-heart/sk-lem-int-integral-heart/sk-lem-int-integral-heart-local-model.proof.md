+++
kind = "proof"
of = "det-lem-int-integral-heart-local-model"
+++
(1) This is the implication from (1) to (3) of [sk-prop-integral-criterion]: by (1)$\Rightarrow$(2)
$K$ is derived complete with $K_1\in\Dbc(X,\mathbf F_E)$, and
[sk-prop-integral-local-structure], (2)$\Rightarrow$(3), gives the stratification and the local models
$K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}M^\bullet$. The tensor product
$M^\bullet\otimes_{\mathcal O_E}\mathcal O_{E,S}$ of a bounded complex of finite free modules is
termwise a finite sum of copies of $\mathcal O_{E,S}$, with differentials given by the matrices
of $M^\bullet$.

(2) *Local form.* Since $\underline{\mathcal O_E}\to\mathcal O_{E,S}$ is flat (\stacks{099L}), on
a local chart of (1) we have $H^q(K)=H^q(M^\bullet)\otimes_{\mathcal O_E}\mathcal O_{E,S}$, the
completion of the finitely generated $\mathcal O_E$-module $H^q(M^\bullet)$. *Membership in
$\Dbc$.* A finitely generated $\mathcal O_E$-module $N$ has a free resolution
$0\to\mathcal O_E^a\to\mathcal O_E^b\to N\to0$, in degrees $-1,0$. Tensoring it with
$\mathcal O_{E,S}$ is still exact by flatness, so on the same charts $H^q(K)$ is
$\mathcal O_{E,S}\otimes_{\mathcal O_E}[\mathcal O_E^a\to\mathcal O_E^b]$, a local model as in
condition (3) of [sk-prop-integral-criterion] on the strata of (1). By (3)$\Rightarrow$(1) of
that proposition, $H^q(K)\in\Dbc(X,\mathcal O_E)$; in particular it is derived complete.

(3) $K$ is bounded, so each truncation is obtained from finitely many $H^q(K)[-q]$ by
successive extensions (triangles $\tau_{\le q-1}\to\tau_{\le q}\to H^q[-q]$). Since
$\Dbc(X,\mathcal O_E)$ is closed under shifts and extensions (both conditions of (2) in
[sk-prop-integral-criterion] are), the truncations lie in it.
