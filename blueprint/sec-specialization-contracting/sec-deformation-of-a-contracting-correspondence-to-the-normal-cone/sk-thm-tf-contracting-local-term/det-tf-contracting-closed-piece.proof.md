+++
kind = "proof"
of = "det-tf-contracting-closed-piece"
uses = ["det-tf-contracting-restricted-morphism", "det-tf-contracting-vanishing", "det-tf-fixed-ideal-nilpotent", "prop-trf-trace-class-additivity", "thm-trf-trace-proper-compatibility"]
+++
Let $j:X\setminus Z_{\mathrm{red}}\hookrightarrow X$ and consider the open–closed triangle
$j_!j^*K\to K\to Ri_*i^*K$. The ideal inclusion $L\subset J$ gives
$c_1^{-1}(Z_{\mathrm{red}})\subset c_2^{-1}(Z_{\mathrm{red}})$, which is the invariance
hypothesis of the additivity of trace classes ([prop-trf-trace-class-additivity]). It gives

$$
 \operatorname{Tr}_c(u)=\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u''),
$$

where $u'$ and $u''$ are the coefficient morphisms induced on $j_!j^*K$ and on $Ri_*i^*K$.

The open piece $j_!j^*K$ restricts to zero on $Z_{\mathrm{red}}$, so
[det-tf-contracting-vanishing] gives $\operatorname{Tr}_c(u')=0$.

By the construction in the additivity statement, the closed piece $u''$ is the proper
pushforward along $(i,e)$ of the restricted correspondence, whose coefficient morphism is $u_Z$ of
[det-tf-contracting-restricted-morphism]. The proper-pushforward compatibility of trace classes
([thm-trf-trace-proper-compatibility]) identifies $\operatorname{Tr}_c(u'')$ with
$h_*\operatorname{Tr}_{c_Z}(u_Z)$.

The map $h$ is the closed immersion $F_{c_Z}=F_c\times_CC_Z\to F_c$. By
[det-tf-fixed-ideal-nilpotent], $F_c$ maps into $Z$ up to nilpotents, so $F_c\cap c_1^{-1}(Z)$ has
the same reduction as $F_c$, and $h$ is an isomorphism after reduction; its pushforward identifies
the dualizing sections. If $F_c$ is proper, integrating both sides and composing the exceptional
counits gives the equality of local terms.
