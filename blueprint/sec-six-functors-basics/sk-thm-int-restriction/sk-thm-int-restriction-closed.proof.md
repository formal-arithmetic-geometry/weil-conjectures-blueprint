+++
kind = "proof"
of = "det-thm-int-restriction-closed"
+++
Let $j:U\hookrightarrow X$ be the open complement, quasi-compact since $X$ is
Noetherian. The localization triangle
$i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to$ exists for
$\mathcal O_{E,X}$-modules with the same proof as in
[det-prop-closed-adjoint-constructible-support] (the formal properties of
$R\underline\Gamma_Z$, [sk-lem-formal-closed-support], hold for any sheaf of
rings). Its third term lies in $\Dbc(X,\mathcal O_E)$ by
[det-thm-sf-pf-adic-open], so the first does, and
$R\underline\Gamma_ZK\simeq i^*i_*R\underline\Gamma_ZK\in\Dbc(Z,\mathcal O_E)$,
since $i^*$ preserves integral constructibility. The Yoneda argument of
[det-prop-closed-adjoint-constructible-yoneda] applies verbatim: for $A$ in
$\Loc(\Dbc(Z,\mathcal O_E))$, both $\Hom(A,i^!K)$ and
$\Hom(A,R\underline\Gamma_ZK)$ are identified with $\Hom(i_*A,K)$ through the
counits, using $Ri_!=i_*$ and that the localizing categories are full
subcategories of the pro-étale derived categories. Hence
$i^!K\simeq R\underline\Gamma_ZK$, naturally in $K$.
