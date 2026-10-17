+++
kind = "proof"
of = "sk-lem-tf-independent-base-change"
uses = ["sk-thm-nagata-compactification", "sk-cor-geo-open-finiteness", "sk-thm-properbasechange"]
+++
Since $T$ may be singular, smooth base change is not available, and the base change
for open direct images over the ground field takes its place.

Choose a compactification $f=\bar fj$, with $j:X\hookrightarrow\bar X$ open and
$\bar f:\bar X\to Y$ proper (Theorem [sk-thm-nagata-compactification]). By
Corollary [sk-cor-geo-open-finiteness], $Rj_*M$ is bounded constructible and its
formation commutes with the base change $\bar X\times T\to\bar X$ along the
finite-type $k$-scheme $T$. Proper base change [sk-thm-properbasechange] gives the
same for $R\bar f_*$. Their composite is the stated map, by the composition law for
ordinary base change.
