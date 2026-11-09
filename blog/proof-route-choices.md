+++
title = "Notes on Proof Route Choices in the Weil Conjectures Blueprint"
author = "Xiangyu Pan"
date = "October 2026"
+++

*PDF version:* <a href="files/NOTES%20ON%20PROOF%20ROUTE%20CHOICES.pdf" download>NOTES ON PROOF ROUTE CHOICES.pdf</a>

*Abstract.* We explain the rationale behind the choice of constructions and
proofs in our blueprint for the Weil conjectures. Our approach favors ordinary
categories, the reuse of existing foundations, and a small collection of widely
applicable tools.

This note records the rationale behind our proof-route choices in the Weil
conjectures. We first state the general principles that guide the proof as a
whole ([§1](#sec-1)), then discuss the choices made for individual topics ([§2](#sec-2)). The route
itself uses modern methods for a good part of the argument, some of which have
not been written down in this setting before.

## <span id="sec-1"></span>1. Guiding principles

**Ordinary categories.** We work only with 1-categories. Using higher category
theory, such as 2-categories or $\infty$-categories, would make the proof depend
on an unnecessarily large input; formalizing it would also considerably enlarge
the project without being necessary for the results we use.

**Avoiding local acyclicity and vanishing cycles.** We avoid the general
formalism of local acyclicity and of nearby and vanishing cycles [[SGA7II](#ref-SGA7II), Exp.
XIII]. Besides its technical geometric inputs, this formalism introduces
delicate functoriality and equivariance issues. In the derived 1-category,
taking a cone is not in general functorial, so defining vanishing cycles as a
cone does not by itself provide their functoriality; higher-categorical
enhancements express this functoriality and its coherences more naturally.
Avoiding this formalism therefore keeps the proof within our chosen foundations
and reduces the work needed to manage Galois actions and specialization.

**Weil II and $\ell$-adic coefficients.** We choose the route via weight theory
in *Weil II* [[D2](#ref-D2)] over the route via Lefschetz pencils in *Weil I*
[[D1](#ref-D1)]: the result of *Weil II* is more general than that of *Weil
I*; weight theory and the Fourier transform tend to be used more broadly in the
literature than Lefschetz-pencil theory; and the improved Fourier-transform
proof adopted here avoids vanishing cycles ([§2.6](#sec-2-6)), whereas the Lefschetz-pencil
proof relies on them.

For coefficients we choose $\ell$-adic, specifically pro-étale, cohomology.
Pro-étale cohomology is already available in Mathlib, and the `proetale`
repository [[JM](#ref-JM)] formalizes the comparison theorems with étale cohomology, so
this material can be reused rather than developed from scratch. By contrast,
the $p$-adic alternative relevant here is rigid cohomology, which would require
developing a separate foundation, including rigid analytic spaces.

## <span id="sec-2"></span>2. Choices for individual topics

The choices below are grouped by topic; each records what we chose and why.

### 2.1. Constructible derived categories

**Pro-étale rather than classical adic systems.** The pro-étale topology of
Bhatt–Scholze [[BS](#ref-BS), §§3–6] gives a cleaner treatment of adic coefficients.
Classically, coefficients are encoded by systems of étale sheaves; in the
pro-étale setting, one has repleteness and actual coefficient sheaves
$\mathcal{O}_{E,X}$ and $E_X$ for an arbitrary algebraic extension
$E/\mathbb{Q}_\ell$. This makes the constructible categories more natural to
formulate. In the noetherian setting it also simplifies the definitions and
provides a uniform foundation for the six functors needed later [[BS](#ref-BS), §6.8].

**The condensed approach.** We also use the perspective of
Hemo–Richarz–Scholbach [[HRS](#ref-HRS), Def. 3.3, §7], which treats lisse and
constructible objects with finite, $\mathcal{O}_E$- or $E$-coefficients
uniformly on arbitrary schemes. Although their paper is written using
$\infty$-categories, we need only selected results that can be stated and
proved using ordinary categories and derived 1-categories. We adopt these
results for their uniformity and generality without taking on the full
higher-categorical framework of the paper.

### 2.2. Proper and smooth base change

We use the Stacks Project proofs of proper and smooth base change [Stacks, Tags
[`095T`](https://stacks.math.columbia.edu/tag/095T),
[`0EYU`](https://stacks.math.columbia.edu/tag/0EYU)]. The proper-base-change
argument remains close to SGA 4, while the direct smooth-base-change argument
avoids the local-acyclicity formalism used in the classical organization [[SGA4](#ref-SGA4),
Exp. XVI]. Their use of curve cohomology fits well with the Jacobian theory
that is also needed later in this project.

### 2.3. Smooth purity

For purity of smooth pairs, we choose the method of deformation to the normal
cone. It uses normal bundles, vector bundles, and $\mathbb{A}^1$-invariance,
which are useful beyond this particular theorem. This is more rewarding for the
reader, since the same construction is used in intersection theory [[Ful](#ref-Ful), Chap.
5] and homotopy purity [[MV](#ref-MV), §3.2].

### 2.4. The trace formula

**Lefschetz–Verdier rather than curve correspondences.** We use the
Lefschetz–Verdier pairing of SGA 5 [[SGA5](#ref-SGA5), Exp. III]. The Nielsen–Wecken type
route in SGA 4½ [[SGA4½](#ref-SGA4half), *Rapport sur la formule des traces*], also followed by
the Stacks Project [Stacks, Tags
[`03U1`](https://stacks.math.columbia.edu/tag/03U1),
[`03UF`](https://stacks.math.columbia.edu/tag/03UF)], uses Weil’s fixed-point
theorem for curves [[Wei](#ref-Wei)]. Taking that route would require
developing Weil’s classical algebraic geometry and classical, non-derived
intersection theory. The Lefschetz–Verdier pairing instead reuses our
six-functor formalism and is useful for later applications.

**The Künneth formula.** For the ordinary, non-compact-support Künneth formula
needed in the Künneth–Verdier isomorphism, we choose the direct Stacks Project
proof [Stacks, Tag [`0F1P`](https://stacks.math.columbia.edu/tag/0F1P)] to avoid
the general acyclicity machinery. For the pairing itself we follow SGA 5 rather
than the relative formulation of Lu–Zheng [[LZ](#ref-LZ)]: the latter’s
2-categorical framework and broader relative setting would add more work beyond
our application over a finite field.

### 2.5. Weil sheaves

**Rank-one geometric monodromy.** For smooth geometrically connected curves, we
use the proof based on the $\ell$-adic logarithm and Jacobians, which are
already available for computing the cohomology of curves in the proof of the
base change theorems. This replaces the proof in [[D2](#ref-D2), §1.3], which uses class
field theory, and thereby avoids developing it.

**Monodromy and determinant weights.** We use variants of the arguments in [[D2](#ref-D2),
§1.3] that isolate the facts about reductive groups needed for the determinant
weight results. These require some basic results on reductive groups, instead
of the classification of reductive groups.

**The twist lemma.** We use an elementary proof of the twist reduction for
irreducible lisse Weil sheaves, rather than deriving it from the geometric
monodromy results as in [[D2](#ref-D2), Prop. 1.3.14]. This reduces its prerequisites of
the trace formula for Weil sheaves.

### <span id="sec-2-6"></span>2.6. The Deligne–Laumon estimate

We use a further refinement of the Fourier–Deligne approach, taking
Kiehl–Weissauer’s treatment [[KW](#ref-KW), Chap. I] as a reference. This version is not
Laumon’s original argument [[Lau](#ref-Lau)], but a refinement that avoids
vanishing cycles. Compared with Deligne’s original proof [[D2](#ref-D2), §3] and Laumon’s
original development, it has the advantage of a smaller set of prerequisites
compatible with our 1-categorical foundations.

We restrict perverse sheaf theory to the perverse $t$-structure and middle
extension on curves. This is enough for the chosen estimate and avoids the cost
of developing the general theory in all dimensions. The resulting weight
theorem retains the generality that motivated our choice of the Weil II route.

## References

- [<span id="ref-BS">BS</span>] B. Bhatt and P. Scholze, *The pro-étale topology for
  schemes*, Astérisque **369** (2015), 99–201.
  [arXiv:1309.1198](https://arxiv.org/abs/1309.1198).
- [<span id="ref-D1">D1</span>] P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS
  **43** (1974), 273–307.
  [doi:10.1007/BF02684373](https://doi.org/10.1007/BF02684373).
- [<span id="ref-D2">D2</span>] P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS
  **52** (1980), 137–252.
  [doi:10.1007/BF02684780](https://doi.org/10.1007/BF02684780).
- [<span id="ref-Ful">Ful</span>] W. Fulton, *Intersection Theory*, 2nd ed., Ergebnisse der
  Mathematik und ihrer Grenzgebiete (3), vol. 2, Springer-Verlag, Berlin, 1998.
- [<span id="ref-HRS">HRS</span>] T. Hemo, T. Richarz, and J. Scholbach, *Constructible
  sheaves on schemes*, Adv. Math. **429** (2023), article 109179.
  [doi:10.1016/j.aim.2023.109179](https://doi.org/10.1016/j.aim.2023.109179).
- [<span id="ref-JM">JM</span>] J. Jiang and C. Merten, *Proétale cohomology in Lean*, GitHub
  repository, [`https://github.com/chrisflav/proetale`](https://github.com/chrisflav/proetale), accessed 30 October 2026.
- [<span id="ref-KW">KW</span>] R. Kiehl and R. Weissauer, *Weil Conjectures, Perverse
  Sheaves and l’adic Fourier Transform*, Ergebnisse der Mathematik und ihrer
  Grenzgebiete (3), vol. 42, Springer-Verlag, Berlin–Heidelberg, 2001.
  [doi:10.1007/978-3-662-04576-3](https://doi.org/10.1007/978-3-662-04576-3).
- [<span id="ref-Lau">Lau</span>] G. Laumon, *Transformation de Fourier, constantes
  d’équations fonctionnelles et conjecture de Weil*, Publ. Math. IHÉS **65**
  (1987), 131–210. [doi:10.1007/BF02698937](https://doi.org/10.1007/BF02698937).
- [<span id="ref-LZ">LZ</span>] Q. Lu and W. Zheng, *Categorical traces and a relative
  Lefschetz–Verdier formula*, Forum Math. Sigma **10** (2022), e10, 1–24.
  [doi:10.1017/fms.2022.2](https://doi.org/10.1017/fms.2022.2).
- [<span id="ref-MV">MV</span>] F. Morel and V. Voevodsky, *$\mathbb{A}^1$-homotopy theory
  of schemes*, Publ. Math. IHÉS **90** (1999), 45–143.
  [doi:10.1007/BF02698831](https://doi.org/10.1007/BF02698831).
- [<span id="ref-SGA4">SGA4</span>] M. Artin, A. Grothendieck, and J.-L. Verdier (eds.),
  *Théorie des topos et cohomologie étale des schémas*, SGA 4, tomes 1–3,
  Lecture Notes in Mathematics, vols. 269, 270, 305, Springer-Verlag,
  Berlin–New York, 1972–1973.
- [<span id="ref-SGA4half">SGA4½</span>] P. Deligne, *Cohomologie étale*, SGA 4½, avec la collaboration de
  J.-F. Boutot, A. Grothendieck, L. Illusie et J.-L. Verdier, Lecture Notes in
  Mathematics, vol. 569, Springer-Verlag, Berlin–New York, 1977.
- [<span id="ref-SGA5">SGA5</span>] A. Grothendieck (dir.), *Cohomologie $\ell$-adique et
  fonctions L*, SGA 5, edited by L. Illusie, Lecture Notes in Mathematics, vol.
  589, Springer-Verlag, Berlin–New York, 1977.
- [<span id="ref-SGA7II">SGA7II</span>] P. Deligne and N. Katz (eds.), *Groupes de monodromie
  en géométrie algébrique*, SGA 7 II, Lecture Notes in Mathematics, vol. 340,
  Springer-Verlag, Berlin–New York, 1973.
- [<span id="ref-Stacks">Stacks</span>] The Stacks Project Authors, *The Stacks Project*,
  [`https://stacks.math.columbia.edu`](https://stacks.math.columbia.edu), accessed 30 October 2026. Permanent tags
  for individual results are given in the text.
- [<span id="ref-Wei">Wei</span>] A. Weil, *Sur les courbes algébriques et les variétés qui
  s’en déduisent*, Actualités Scientifiques et Industrielles, no. 1041,
  Hermann, Paris, 1948.
