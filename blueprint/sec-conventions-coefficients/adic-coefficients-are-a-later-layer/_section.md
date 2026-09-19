+++
id = "adic-coefficients-are-a-later-layer"
kind = "section"
title = "Adic coefficients are a later layer"
order = 133
+++
The passage from finite torsion coefficients to $\mathbb Z_\ell$, $\mathbb Q_\ell$ and $\overline{\mathbb Q}_\ell$ — derived completion, inversion of
$\ell$, and the colimit over finite extensions of $\mathbb Q_\ell$ — is a
layer built on top of the finite torsion theory. It is assumed nowhere in the
chapters below, and it is not implemented in Lean: the pro-étale site does
not occur in the development, and the coefficients there are always modules
over a ring, never a completed or adic object. In the blueprint it lives
in the proper base change sections S8 (étale-to-pro-étale finite-level
transport), S9 (derived completion and inverse limits) and S10 (complete
pro-étale proper base change) of [chap-proper-base-change], and in the
sketch articles 40–42 (`40_finite_torsion_proetale.tex`,
`41_adic_rational_coefficients.tex`,
`42_qbarl_triangulated_colimit.tex`). A statement in one of those
places is therefore not a statement about the objects the earlier chapters
formalise, and should not be cited as one.
