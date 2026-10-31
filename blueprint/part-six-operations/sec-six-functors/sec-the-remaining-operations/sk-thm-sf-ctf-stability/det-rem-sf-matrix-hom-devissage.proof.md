+++
kind = "proof"
of = "det-rem-sf-matrix-hom-devissage"
+++
We use Noetherian induction on $X$: assume the statement for every proper
closed subscheme of $X$ (with reduced structure) and every pair of objects on
it. The empty scheme is trivial.

*Step 1: a good dense open.* By Stacks, Tag
[0F4M](https://stacks.math.columbia.edu/tag/0F4M), $K$ is represented by a
bounded complex $K^\bullet$ of constructible flat $A$-module sheaves. Each of
the finitely many nonzero terms is finite locally constant on a dense open of
$X$; let $j:U\hookrightarrow X$ be the intersection of these opens and
$i:Z\hookrightarrow X$ its reduced closed complement, a proper closed subset
when $X\neq\emptyset$. On $U$ each $K^q|_U$ is étale locally the constant sheaf
on a finite flat $A$-module; since $A$ is finite (hence Artinian), a finite flat
$A$-module is projective. So $j^*K$ is étale locally a bounded complex $P$ of
finite projective $A$-modules.

*Step 2: the open part.* For such $P$, [lem-sf-hom-finite-projective] applied
termwise (and the finiteness of the complex) shows that the canonical map
$P^\vee\otimes^{\mathbf L}_AN\to R\mathcal Hom_A(P,N)$ is an isomorphism for
every $N$, where $P^\vee$ is the termwise dual, again a bounded complex of
finite projective modules. These local isomorphisms are the restrictions of the
global canonical map
$(j^*K)^\vee\otimes^{\mathbf L}_Aj^*L\to R\mathcal Hom_A(j^*K,j^*L)$, which is
therefore an isomorphism. The complex $(j^*K)^\vee$ is a bounded complex of
constructible flat sheaves, and tensoring a bounded flat constructible model of
$j^*L$ in degrees $[a,b]$ with a flat bounded complex in degrees $[c,e]$ gives
one in degrees $[a+c,b+e]$; hence $R\mathcal Hom_A(j^*K,j^*L)\in\Dctf(U,A)$.
By [lem-weil-stratum-ambient-hom] for $s=j$ (where $Rj_!=j_!$ and
$Rj^!=j^*$),

$$
R\mathcal Hom_A(j_!j^*K,L)\simeq Rj_*R\mathcal Hom_A(j^*K,j^*L),
$$

which lies in $\Dctf(X,A)$ by [cor-fin-deligne-open-finite-coefficients]
(constructibility) and [det-cor-sf-direct-image-ctf-open-tor] (Tor amplitude).

*Step 3: the closed part.* Let $i^!=R\underline\Gamma_Z$ be the right adjoint
of $i_*$. The localization triangle
$i_*i^!L\to L\to Rj_*j^*L\to$ and Step 2's direct-image bound show
$i_*i^!L\in\Dctf(X,A)$; since $i_*$ is exact and $i^*i_*=\mathrm{id}$, and
$i^*$ preserves bounded flat constructible models, $i^!L\simeq i^*i_*i^!L$
lies in $\Dctf(Z,A)$. Likewise $i^*K\in\Dctf(Z,A)$. By
[lem-weil-stratum-ambient-hom] for $s=i$,

$$
R\mathcal Hom_A(i_*i^*K,L)\simeq i_*R\mathcal Hom_A(i^*K,i^!L),
$$

and $R\mathcal Hom_A(i^*K,i^!L)\in\Dctf(Z,A)$ by the induction hypothesis
applied to $Z$. As $i_*$ is exact and carries flat constructible models to flat
constructible models, the left side is in $\Dctf(X,A)$.

*Step 4: gluing.* Apply the exact functor $R\mathcal Hom_A(-,L)$ to the
localization triangle $j_!j^*K\to K\to i_*i^*K\to$. This gives a distinguished
triangle

$$
R\mathcal Hom_A(i_*i^*K,L)\to R\mathcal Hom_A(K,L)\to R\mathcal Hom_A(j_!j^*K,L)\to
$$

whose outer terms lie in $\Dctf(X,A)$ by Steps 2 and 3. Since $\Dctf(X,A)$ is a
triangulated subcategory ([def-weil-finite-tor-amplitude]), the middle term
does too.
