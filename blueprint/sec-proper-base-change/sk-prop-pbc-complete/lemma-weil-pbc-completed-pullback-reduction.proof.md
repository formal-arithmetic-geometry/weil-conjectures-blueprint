+++
kind  = "proof"
of    = "lemma-weil-pbc-completed-pullback-reduction"
+++
(1) The module pullback $g^*$ is exact ([sk-prop-sfb-module-pullback-exact]) and
strong monoidal, and $g^*\mathcal O_{E,T}=\mathcal O_{E,T'}$ because both rings
are pulled back from the point. Applied termwise to the cone
$\operatorname{red}(M)_n=M\otimes[\mathcal O_{E,T}\xrightarrow{\pi_E^n}\mathcal O_{E,T}]$
it gives $g^*M\otimes[\mathcal O_{E,T'}\xrightarrow{\pi_E^n}\mathcal O_{E,T'}]=
\operatorname{red}(g^*M)_n$, compatibly with the transitions; this is an
isomorphism of complexes of towers, natural in $M$
([det-pbc-complete-towers] (3), [det-pe-derived-nakayama-resolution]). Apply
$R\varprojlim$.

(2) By (1) and [det-pbc-complete-derived-completion], applied to $g^*M$ on
$T'$, the object $g^*_{\mathrm{comp}}M=\widehat{g^*M}$ is derived complete and its
reductions are those of $g^*M$, which are $g^*M_n$ by (1), compatibly with the
transitions.

(3) By (1), the map is the completion map of $g^*M$, which is an isomorphism
exactly when $g^*M$ is derived complete ([sk-def-pe-derived-completion]).
