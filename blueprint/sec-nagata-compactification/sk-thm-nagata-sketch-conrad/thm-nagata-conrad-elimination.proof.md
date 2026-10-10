+++
kind  = "proof"
of    = "thm-nagata-conrad-elimination"
+++
The density of $U$ is not used below.

If $p$ is quasi-affine in the sense of [def-nagata-quasi-affine-morphism],
this is [lemma-nagata-conrad-quasi-affine-general]: its finite type ideal
$\mathcal I$ with $V(\mathcal I)\cap V=\varnothing$ defines a
$V$-admissible blow-up, and it supplies $W\supseteq\pi^{-1}(U)$ and the
extension $g$ with closed graph.

In general, let $q\colon\widetilde X\to X$ be the $V$-admissible blow-up and
$\sigma\colon U\hookrightarrow\widetilde X$ the open immersion with
$q\circ\sigma$ the inclusion of $U$ produced by
[lemma-nagata-conrad-graph-closure-quasi-finite], let
$F=(f,\sigma)\colon U\to Y\times_X\widetilde X$, and let
$Z=\overline{F(U)}\subseteq Y\times_X\widetilde X$ be the scheme-theoretic
image of $F$, with closed immersion $i\colon Z\hookrightarrow Y\times_X\widetilde X$
and $p_Z=\mathrm{pr}_{\widetilde X}\circ i\colon Z\to\widetilde X$. That lemma
makes $p_Z$ locally quasi-finite, locally of finite type, quasi-compact and
separated, so [lemma-nagata-quasi-affine-morphism-of-quasi-finite] makes $p_Z$
quasi-affine as a morphism. (Neither $\widetilde X$ nor $Z$ need be
quasi-affine as a scheme, so only the relative form of quasi-affineness is
available here.)

We now check the hypotheses of [lemma-nagata-conrad-quasi-affine-general]
over $\widetilde X$. The blow-up $q$ is proper
([lemma-nagata-blowup-proper]), so $\widetilde X$ is quasi-compact and
quasi-separated, and $q^{-1}(U)\subseteq q^{-1}(V)$ are quasi-compact opens.
The scheme $Z$ is quasi-compact and quasi-separated, since $p_Z$ is
quasi-compact and separated over the qcqs scheme $\widetilde X$. Since the
centre of $q$ is disjoint from $V\supseteq U$, $q$ restricts to an
isomorphism $q^{-1}(V)\to V$ (apply
[lemma-nagata-affine-blowup-complement] on an affine open cover of $V$), and
$\sigma$ is an isomorphism of $U$ onto $q^{-1}(U)$, inverse to $q$ there. Let
$f'\colon q^{-1}(U)\to Y\times_X\widetilde X$ be the base change of $f$, i.e.
the section of the projection $p'\colon Y\times_X\widetilde X\to\widetilde X$
over $q^{-1}(U)$ induced by $f\circ q|_{q^{-1}(U)}$. Under
$\sigma\colon U\cong q^{-1}(U)$ it is $F$, so $f'$ factors through $Z$ as
$f'=i\circ f''$ with $f''\colon q^{-1}(U)\to Z$ a section of $p_Z$ over
$q^{-1}(U)$. Over $q^{-1}(V)\cong V$ the morphism $p'$ is identified with
$p^{-1}(V)\to V$ and the image of $f'$ with the image of $f$, which is
closed in $p^{-1}(V)$; hence the image of $f'$ is closed in
$p'^{-1}(q^{-1}(V))$, and the image of $f''$, being its inverse image under
$i$, is closed in $p_Z^{-1}(q^{-1}(V))$.

So [lemma-nagata-conrad-quasi-affine-general] applies to
$(\widetilde X,\,q^{-1}(U)\subseteq q^{-1}(V),\,p_Z,\,f'')$ and gives a
$q^{-1}(V)$-admissible blow-up of $\widetilde X$ together with an open
containing the inverse image of $q^{-1}(U)$ and an extension of $f''$ with
closed graph. By [lemma-nagata-conrad-closed-target-reduction] applied to the
closed immersion $i$ (with $p'\circ i=p_Z$), the data
$(\widetilde X,q^{-1}(U),q^{-1}(V),p',f'=i\circ f'')$ admit an extension
in the sense of [lemma-nagata-conrad-blowup-base-change-reduction]. By that
lemma, applied to the $V$-admissible blow-up $q$, the original data
$(X,U,V,p,f)$ admit an extension, which is the assertion.
