+++
kind  = "proof"
of    = "lemma-nagata-strict-transform-restrict"
uses = ["def-nagata-extended-ideal", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-strict-transform-over-complement", "thm-nagata-global-blowup-complement"]
+++
By [thm-nagata-global-blowup-complement] the blow-up restricts to an
isomorphism $b^{-1}(X\setminus C)\xrightarrow{\sim}X\setminus C$, so
[lemma-nagata-strict-transform-over-complement] shows that $\Omega$, with
its projection to $Y$ and the map to $X\setminus C$, is a fibre product of
$f$ and $X\setminus C\hookrightarrow X$. It remains to see that the strict
transform contains all of $\Omega$, i.e. that the projection
$\widetilde Y\times_{Y\times_XX'}\Omega\to\Omega$ is an isomorphism. This
projection is a closed immersion. Since $\widetilde Y$ is the
scheme-theoretic image ([def-nagata-scheme-theoretic-image]) of the open
immersion $j\colon\Omega\hookrightarrow Y\times_XX'$, its ideal is the
kernel ideal of $j$ ([lemma-nagata-scheme-image-ideal-qc]), and the ideal
of the projection is the extension of that kernel ideal along $j$
([def-nagata-extended-ideal]). This extension is zero because
$j^\sharp$ restricted to $\Omega$ is the identity of $\mathcal O_\Omega$.
A closed immersion with zero ideal is an isomorphism, and transporting the
fibre square of $\Omega$ along it gives the claim.
