+++
id = "a43.-dense-compactifications-and-composition"
kind = "section"
title = "A43. Dense compactifications and composition"
order = 905
+++
Let $f:X\to Y$ be separated and finitely presented. A dense
compactification is data

$$
C=(X\xrightarrow{j_C}\overline X_C\xrightarrow{p_C}Y,
\epsilon_C:p_C\circ j_C=f),
\tag{BA43-DENSE-DATA}
$$

where $j_C$ is a schematically dense open immersion and $p_C$ is proper and
finitely presented. The equality $\epsilon_C$ is stored structure data. A
refinement $q:D\to C$ is a $Y$-map with $qj_D=j_C$ and
$q^{-1}(X)=X$. Its properness is a separate geometric atom.

Before any constructible restriction, set

$$
F_C^{\mathrm{amb}}=Rp_{C*}Rj_{C!}:
D^+(X_{\acute et},\Lambda_n)\longrightarrow
D^+(Y_{\acute et},\Lambda_n).
\tag{BA43-AMBIENT-F}
$$

All $F_C$ and all selected $Rf_!$ in this fragment denote these ambient
functors. A restriction to $D_c^+$ is a separate theorem. Consequently
$Rg_!^{\mathrm{amb}}Rf_!^{\mathrm{amb}}$ is typed before any assertion that
$Rf_!K$ is constructible.

The refinement middle owner constructs

$$
\gamma_q:Rq_*Rj_{D!}\xrightarrow{\sim}Rj_{C!},
\qquad
\rho_q:R(p_Cq)_*Rj_{D!}\xrightarrow{\sim}Rp_{C*}Rj_{C!},
\tag{BA43-RHO}
$$

and proves identity, composition, and required naturality. It also constructs
the same proper-support comparison $\rho_q^{\mathrm{raw}}$ for a proper map
between typed raw models that is the identity over the source open; density is
not used for that construction. Only dense models enter the following
$\kappa$ system. For a common
dense refinement $E$, set

$$
\kappa_{C,D}=\rho_{E\to D}\,\rho_{E\to C}^{-1}.
$$

Schematic-density uniqueness, common refinement, and the equations for
$\rho$ must prove independence of $E$ and the $\kappa$ cocycle.

**Formalization note.** The comparison map of (BA43-RHO) is now constructed in Lean, in the
bounded below variant, as
`AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison`
(`WeilConjectures/SixFunctors/Derived/LowerShriekComparison.lean`), for a refinement
whose square over the source open is Cartesian, and both of its functoriality laws are proved in
that same file. The identity law
`AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id`
says that the comparison attached to the identity refinement of a compactification is the
identity natural transformation; the composition law
`AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp`
says that for refinements `r : c.Refinement d` and `s : d.Refinement e` whose
squares over the source open are Cartesian, the comparison attached to `r.comp s`, taken
for the pasted square
`AlgebraicGeometry.Compactification.Refinement.isPullback_comp` of
`WeilConjectures/Compactification/RefinementPullback.lean`, is the comparison of
`s` followed by the comparison of `r` — in that order and not the reverse, the
formalized map being contravariant in the refinement, for the reason given next. It is still
not known to be an isomorphism, and the further naturality that (BA43-RHO) asks for is
not formalized either. The isomorphism property is exactly what
`OBL-BA43-REFINEMENT-EXCHANGE` demands, it needs proper base change, and it remains open,
as does the $\kappa$ system built on it.

**The formalized arrow points the other way.** It goes from the coarser model to
the finer one, $Rp_{C*}Rj_{C!}\to R(p_Cq)_*Rj_{D!}$ in the lettering above, that is
$F_C\to F_D$, the reverse of the $\rho_q$ displayed here. (In Lean a refinement is written
`r : c.Refinement d` with `c` the finer model, so the declaration reads
$Rf_!(d)\to Rf_!(c)$, coarse to fine.) This is deliberate. Neither direction is formal: the
available adjunctions produce a *cospan*, both of whose legs point into
$Rp_{C*}Rq_*Dq^*Rj_{C!}$, so an arrow between $F_C$ and $F_D$ exists only once one leg is
inverted. Inverting the leg that yields the direction displayed above is precisely proper base
change; inverting the other leg, the base change isomorphism
$Rj_{D!}\xrightarrow{\sim}Dq^*Rj_{C!}$ coming from $q^{-1}(X)=X$, is what the Cartesian
hypothesis supplies, and it yields the opposite arrow. So the direction constructible without
proper base change is the reverse of the blueprint's. The two maps are mutually inverse as soon
as both legs are isomorphisms, so the reversal changes no mathematical content.

The declaration is the bounded below (`Plus`) comparison only. No unbounded
variant is formalized: there is no unbounded $Dq^*\dashv Rq_*$ adjunction in this repository, and
the unbounded composition isomorphism for $Rp_*$ rests on the still `sorry`ed
`HasKInjectiveResolutions`.

For $X\xrightarrow fY\xrightarrow gZ$, a successive witness includes a
Cartesian square

$$
\begin{array}{ccc}
\overline X_f&\xrightarrow{u\ \mathrm{schematically\ dense\ open}}&W\\
\mathllap{p_f}\downarrow&&\downarrow\mathrlap{\bar p\ \mathrm{proper}}\\
Y&\xrightarrow{j_g}&\overline Y_g
\end{array}
$$

and a stored equality proving that $u\circ j_f:X\to W$ is schematically
dense. The open–proper exchange

$$
Rj_{g!}Rp_{f*}\xrightarrow{\sim}R\bar p_*Ru_!
\tag{BA43-OPX}
$$

must satisfy refinement naturality and typed two-square and three-square
pasting. The separately constructed isomorphism

$$
Ru_!Rj_{f!}\xrightarrow{\sim}R(u\circ j_f)_!
$$

has unit, composition, and pentagon laws. Two-witness independence and triple
pasting then reassemble the choice-independent comparison
$Rg_!Rf_!\to R(gf)_!$. Thus
`OBL-BA43-RELATIVE-COHERENT-CORE` remains
`OPEN/INCOMPLETE`.
