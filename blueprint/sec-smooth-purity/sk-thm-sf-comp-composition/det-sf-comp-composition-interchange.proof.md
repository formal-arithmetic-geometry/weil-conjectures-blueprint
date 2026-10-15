+++
kind = "proof"
of = "det-sf-comp-composition-interchange"
uses = ["det-sf-comp-coherence-single", "det-sf-determination-localizing", "sk-prop-proper-base-change-unbounded"]
+++
*(1)* The open immersion $j'$ factors through the open subscheme
$r^{-1}(Y)\subset W$ because $r j'=i p$ lands in $Y$. The induced
$\overline X\to r^{-1}(Y)$ is a $Y$-morphism from the proper $Y$-scheme
$\overline X$ to the separated $Y$-scheme $r^{-1}(Y)$ (separated since $r$ is
proper), hence proper, so its image is closed in $r^{-1}(Y)$. It is also open,
and dense because $\overline X$ is dense in $W$. An open, closed, dense subset
of $r^{-1}(Y)$ is all of it; so $\overline X=r^{-1}(Y)$ and $r|_{r^{-1}(Y)}=p$.

*(2)* Restriction $i^*$ to the open $Y$ commutes with $Rr_*$ (it has the exact
left adjoint $i_!$, so preserves K-injectives), giving by (1)
$i^*Rr_*j'_!A\simeq Rp_*(j'^*j'_!A)\simeq Rp_*A$. Under $i_!\dashv i^*$, maps
$i_!Rp_*A\to Rr_*j'_!A$ correspond bijectively to maps
$Rp_*A\to i^*Rr_*j'_!A\simeq Rp_*A$, the correspondence being restriction to
$Y$; take $\iota_A$ to correspond to the identity.

*(3)* Let $c:\overline Y\setminus Y\to\overline Y$ be the closed complement. For
$A\in\Dctf(\overline X,\Lambda)$: over $Y$, $\iota_A$ is the identity. Over the
complement, $c^*i_!Rp_*A=0$, and by proper base change for $r$ along $c$
([sk-prop-proper-base-change-unbounded]),
$c^*Rr_*j'_!A\simeq R(r_c)_*(j'_!A)|_{r^{-1}(\overline Y\setminus Y)}=0$, because
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$ by (1) and $j'_!A$ vanishes
there. The pair $(i^*,c^*)$ detects isomorphisms (open–closed exact sequence,
Stacks, Tag 09AH), so $\iota_A$ is an isomorphism. Both $A\mapsto i_!Rp_*A$ and
$A\mapsto Rr_*j'_!A$ are exact functors on $\Loc(\Dctf(\overline X,\Lambda))$
preserving direct sums ([det-sf-comp-coherence-single]) and $\iota$ is a natural
transformation of exact functors (by the uniqueness in (2), it commutes with
shifts and with morphisms of $A$); by [det-sf-determination-localizing] it is an
isomorphism on all of $\Loc(\Dctf(\overline X,\Lambda))$.
