+++
kind = "proof"
of = "det-sp-p1-trace"
uses = ["thm-amb-p1-decomposition", "def-amb-p1-trace", "lem-amb-p1-diagonal-integrals"]
+++
*(1)* This is [thm-amb-p1-decomposition] on the étale site, transported to the
pro-étale site by the comparison (both sides are classical, and the
comparison identifies derived direct images and cohomology classes). On a
geometric fibre, $H^0(\mathbf P^1,\Lambda_n)=\Lambda_n$, $H^1=0$, and
$H^2(\mathbf P^1,\Lambda_n(1))=\operatorname{Pic}(\mathbf P^1)/\ell^n=\Lambda_n$ generated
by $h$ (Kummer sequence), and $H^q=0$ for $q>2$; by proper base change the map
$(1,h)$ is an isomorphism on every geometric stalk of every cohomology sheaf.
The class $h$ pulls back to the class of $\mathcal O(1)$ under any base change, and
proper base change is compatible with pullback of classes, so $(1,h)$ commutes
with base change.

*(2)* After twisting by $(1)[2]$, (1) reads
$(\Lambda_n)_S(1)[2]\oplus(\Lambda_n)_S\simeq Rq_*(\Lambda_n)(1)[2]$, the second
summand being spanned by $h$; $\operatorname{Tr}_q$ is the projection onto it
([def-amb-p1-trace]), so $\operatorname{Tr}_q(h)=1$. Base-change compatibility
follows from that of (1). On a geometric fibre, a rational point $x$ has
$\mathcal O(x)\simeq\mathcal O(1)$, so its class is $h$ and its trace is $1$.

*(3)* $\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta$ is an endomorphism of the sheaf
$(\Lambda_n)_P$ in degree zero, so a morphism of sheaves, determined by its
geometric stalks. By proper base change the stalk at $\bar x$ is the trace,
on the fibre $\mathbf P^1_{\bar x}$ of $p_i$, of the cycle class of the single
rational point cut out by $\Delta$; by (2) it is $1$. This is
[lem-amb-p1-diagonal-integrals].
