+++
kind = "proof"
of = "det-pe-sections-limits-colimits"
+++
*Limits.* Limits of sheaves of modules are computed sectionwise, so $\Gamma(W,-)$ preserves
them.

*Direct sums.* Let $P$ be the presheaf $V\mapsto\bigoplus_iM_i(V)$; then
$\bigoplus_iM_i=P^{\#}$. For a finite subset $J\subset I$, the finite sum
$\bigoplus_{i\in J}M_i=\prod_{i\in J}M_i$ is already a sheaf, and it is a subsheaf of
$P^{\#}$ (the presheaf inclusion $\bigoplus_JM_i\to P$ is injective and sheafification is
exact).

Surjectivity: let $s\in P^{\#}(W)$. Every section of a sheafification is locally a section
of the presheaf, so there are a covering $\{V_k\to W\}$ and $p_k\in P(V_k)$ with
$s|_{V_k}=p_k$. Since $W$ is affine, the covering condition
[def-weil-pbc-proetale-covering] gives finitely many affine opens of members of the
covering whose images cover $W$; they form a finite covering $\{V'_l\to W\}$ refining the
first one, and restricting the $p_k$ gives $p'_l\in P(V'_l)$. Each $p'_l$ has finite
support, so there is one finite $J\subset I$ with $p'_l\in\bigoplus_{i\in J}M_i(V'_l)$ for
all $l$. The $p'_l$ are compatible in $P^{\#}$, hence in the subsheaf
$\bigoplus_JM_i$, so they glue to $t\in(\bigoplus_JM_i)(W)=\bigoplus_{i\in J}M_i(W)$. Its
image in $P^{\#}(W)$ agrees with $s$ on the covering, hence equals $s$.

Injectivity: an element of $\bigoplus_iM_i(W)$ lies in $\bigoplus_{i\in J}M_i(W)$ for some
finite $J$, and $(\bigoplus_JM_i)(W)\to P^{\#}(W)$ is injective because
$\bigoplus_JM_i\subset P^{\#}$ is a subsheaf.

*Colimits.* A colimit of $\mathcal R$-modules is the cokernel of a map between direct sums
$\bigoplus_{\alpha\to\beta}M_\alpha\to\bigoplus_\gamma M_\gamma$. $\Gamma(W,-)$ preserves
both direct sums and cokernels, the latter because it is exact
([det-pe-wc-sections-exact], valid for every weakly contractible $W$ by part 3 of
[det-pe-weak-contractible-equivalences]); hence it preserves the colimit. Filtered
colimits are a special case.
