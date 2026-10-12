+++
kind  = "proof"
of    = "lem-sfb-constructible-cocone-hom-surj"
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-def-sfb-constructible", "lem-sfb-qlbar-flat", "def-sfb-derived-extend-comp-iso"]
+++
Replacing $E$ and $F$ by a common finite extension containing both (using the transitivity
isomorphisms of [def-sfb-derived-extend-comp-iso]) we may assume $E=F$. The claim is then the
surjectivity in the continuity of the derived hom:

$$
\operatorname{colim}_{H\supseteq E}\Hom_{D(\Mod_{H_X})}(T_{E,H}K,T_{E,H}L)
\longrightarrow\Hom_{D(\Mod_{\overline{\mathbf Q}_{\ell,X}})}(T_{E,\Qlb}K,T_{E,\Qlb}L).
$$

By the adjunction $T\dashv D(\operatorname{Res})$ both sides are homs in $D(\Mod_{E_X})$ out of
$K$, into $T_{E,H}L$ resp. into $T_{E,\Qlb}L$. All extensions of scalars are exact
([lem-sfb-qlbar-flat]), so $T_{E,\Qlb}L=\operatorname{colim}_HT_{E,H}L$ termwise
([sk-prop-sfb-qlbar-colimit-x]), a filtered colimit of uniformly bounded below complexes.
Since $X$ is Noetherian, $K$ is a finite iterated extension of shifts of modules that are
locally finitely presented on the strata of a finite stratification
([sk-def-sfb-constructible]); for such modules, and hence for $K$ (five lemma), the derived hom
into a filtered colimit of uniformly bounded below complexes is the filtered colimit of the
derived homs. Hence the map above is bijective, in particular surjective.
