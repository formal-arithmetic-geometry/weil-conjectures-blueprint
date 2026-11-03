+++
kind  = "proof"
of    = "lem-pc-f-open-subfunctor"
+++
*The open locus of a single class.* Let $T$ be a scheme over $k$ and
$\mathcal{L}\in\operatorname{Pic}_{X/k,\sigma}(T)$, represented by an invertible
module $\mathcal L$ on $X_T$. The morphism $f_T:X_T\to T$ is proper of finite
presentation, being the base change of $X\to\operatorname{Spec} k$, and
$\mathcal{L}$ is of finite presentation and flat over $T$: $\mathcal{L}$ is
locally free, $f_T$ is smooth hence flat [lem-pc-smooth-flat], and flat
morphisms compose. Apply [lem-pc-flat-rf-open] with $f=f_T$,
$\mathcal{F}=\mathcal{L}$, $i=0$, $r=1$: there is an open $U\subseteq T$ such
that a morphism $u:T'\to T$ of $k$-schemes factors through $U$ if and only if
$Rf_{T',*}\mathcal{L}_{T'}$ is isomorphic to a finite locally free
$\mathcal{O}_{T'}$-module of rank $1$ placed in degree $0$ (here
$X_T\times_TT'=X_{T'}$, so the base change of $f_T$ along $u$ is $f_{T'}$ and
the pullback of $\mathcal L$ is $\mathcal L_{T'}=u_X^*\mathcal L$). As a finite
locally free module of rank $1$ is an invertible module
([def-sc-invertible-module]), this says: $u$ factors through $U$ if and only
if $\mathcal{L}_{T'}\in F(T')$.

*$F$ is a subfunctor.* Let $\mathcal{L}\in F(T)$ and let $u:T'\to T$ be a
morphism. Taking for $u$ the identity of $T$ in the criterion above shows
that $\mathrm{id}_T$ factors through $U$, i.e. $U=T$. Hence every $u:T'\to T$
factors through $U$, and $\mathcal{L}_{T'}\in F(T')$.

*$F$ is open.* The open $U=U_\xi$ attached to $\xi=\mathcal{L}$ has, by the
criterion, exactly the property required in [def-pc-subfunctor]: a morphism
$u:T'\to T$ factors through $U_\xi$ if and only if $u^*\xi\in F(T')$. Hence
the inclusion $F\subseteq\operatorname{Pic}_{X/k,\sigma}$ is representable by
open immersions.
