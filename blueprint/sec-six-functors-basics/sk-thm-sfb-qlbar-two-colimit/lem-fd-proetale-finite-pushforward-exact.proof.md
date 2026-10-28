+++
kind = "proof"
of = "lem-fd-proetale-finite-pushforward-exact"
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-thm-pe-weakly-contractible-basis", "sk-def-pe-weak-contractible", "sk-lem-pe-weakly-etale-stability", "det-prop-sfb-module-category", "def-sfb-module-lower-star", "det-def-sfb-module-derived-pushpull"]
+++
This is Bhatt–Scholze, *The pro-étale topology for schemes*, Lemma 6.1.17; we
recall the argument.

*(1).* As a right adjoint ([sk-def-sfb-finite-pushforward-pullback]), $f_*$
preserves kernels, so it suffices to show that it preserves epimorphisms. Every
object of $Y_{\mathrm{proét}}$ is covered by affines $W=\operatorname{Spec}D$ with
$D$ w-contractible ([sk-thm-pe-weakly-contractible-basis]), so a morphism of
sheaves on $Y_{\mathrm{proét}}$ is an epimorphism as soon as it is surjective on
sections over every such $W$. For such $W$, the base change
$W\times_YX\to X$ is weakly étale ([sk-lem-pe-weakly-etale-stability]), and
$W\times_YX=\operatorname{Spec}D'$ with $D\to D'$ finite of finite presentation.
Hence $D'$ is w-contractible (Bhatt–Scholze, Lemma 2.4.10), and $W\times_YX$ is a
weakly contractible object of $X_{\mathrm{proét}}$
([sk-thm-pe-weakly-contractible-basis]). Let $G\to H$ be an epimorphism of sheaves
of $R$-modules on $X_{\mathrm{proét}}$. By weak contractibility
([sk-def-pe-weak-contractible]) the map
$(f_*G)(W)=G(W\times_YX)\to H(W\times_YX)=(f_*H)(W)$ is surjective. So $f_*G\to f_*H$
is an epimorphism.

*(2).* The underlying abelian sheaf of $f_*M$ is $f^{\Ab}_*M$
([def-sfb-module-lower-star]), and the forgetful functor
$\Mod_{\Lambda_X}\to\Sh(X_{\mathrm{proét}},\Ab)$ is exact and faithful, with kernels
and cokernels computed on underlying sheaves ([det-prop-sfb-module-category], (1)
and (4)). A sequence of module objects is therefore exact if and only if its
underlying sequence of abelian sheaves is, and exactness of $f_*$ on
$\Mod_{\Lambda_X}$ follows from (1) with $R=\mathbf Z$. An exact functor preserves
cohomology of complexes, hence quasi-isomorphisms. If $K\to I$ is a K-injective
resolution, then $f_*K\to f_*I=Rf_*K$ ([det-def-sfb-module-derived-pushpull]) is a
quasi-isomorphism, so $Rf_*K\simeq f_*K$. For a module $M$ placed in degree $0$
this gives $R^qf_*M=0$ for $q>0$.
