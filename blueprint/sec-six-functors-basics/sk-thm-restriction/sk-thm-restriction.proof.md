+++
kind = "proof"
of = "sk-thm-restriction"
uses = ["sk-lem-sf-mate", "sk-cor-affine-space-rational", "sk-prop-closed-adjoint-constructible", "sk-prop-sf-comp-coherence", "sk-prop-sf-existence"]
+++
Let $K\in\Dbc(Y,\Lambda)$. Cover $Y$ by finitely many affine opens
$V_\beta$, and each $f^{-1}(V_\beta)$ by finitely many affine opens
$U_{\beta\alpha}$. Since $f$ is of finite type, each $U_{\beta\alpha}$ admits a
closed immersion $i:U_{\beta\alpha}\hookrightarrow\mathbf A^d_{V_\beta}$ over
$V_\beta$. With $p:\mathbf A^d_{V_\beta}\to V_\beta$ the projection and
$u:U_{\beta\alpha}\hookrightarrow X$, $v:V_\beta\hookrightarrow Y$ the
inclusions, we have $f\circ u=v\circ p\circ i$. By [sk-lem-sf-mate], as
functors $\Loc(\Dbc(Y,\Lambda))\to\Loc(\Dbc(U_{\beta\alpha},\Lambda))$,

$$
u^*f^!\simeq(fu)^!=(vpi)^!\simeq i^!p^!v^*.
$$

Now $v^*K$ is bounded constructible, so $p^!v^*K$ is bounded constructible by
[sk-cor-affine-space-rational], and $u^*f^!K\simeq i^!p^!v^*K$ is bounded
constructible by [sk-prop-closed-adjoint-constructible].

Both conditions defining $\Dbc$ are local for a finite open cover. The
cohomology of $f^!K$ vanishes outside the union of the finitely many bounded
intervals found on the $U_{\beta\alpha}$. For constructibility, each locally
closed stratum of $U_{\beta\alpha}$ is locally closed in $X$, and a common
refinement of the finitely many resulting finite partitions of $X$ into
locally closed subsets is a stratification on whose strata all cohomology
sheaves of $f^!K$ are lisse. Hence $f^!K\in\Dbc(X,\Lambda)$.

Finally, $Rf_!$ maps $\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$
([sk-prop-sf-comp-coherence]), and $\Dbc(-,\Lambda)\subset\Loc(\Dbc(-,\Lambda))$
is full. So for $A\in\Dbc(X,\Lambda)$ the bijection of [sk-prop-sf-existence]
reads

$$
\Hom_{\Dbc(Y,\Lambda)}(Rf_!A,K)\simeq\Hom_{\Dbc(X,\Lambda)}(A,f^!K).
$$
