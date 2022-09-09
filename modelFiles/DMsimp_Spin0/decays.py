# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 14:17:57


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Y0 = Decay(name = 'Decay_Y0',
                 particle = P.Y0,
                 partial_widths = {(P.a,P.a):'(MY0**2*((8*cw**4*gPb**2*MY0**4)/Lambda**2 + (8*cw**4*gSb**2*MY0**4)/Lambda**2 + (16*cw**2*gPb*gPw*MY0**4*sw**2)/Lambda**2 + (16*cw**2*gSb*gSw*MY0**4*sw**2)/Lambda**2 + (8*gPw**2*MY0**4*sw**4)/Lambda**2 + (8*gSw**2*MY0**4*sw**4)/Lambda**2))/(32.*cmath.pi*abs(MY0)**3)',
                                   (P.a,P.Z):'((MY0**2 - MZ**2)*((8*cw**2*gPb**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gPb*gPw*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gPw**2*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gSb**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gSb*gSw*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gSw**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gPb**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gPb*gPw*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gPw**2*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSb**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gSb*gSw*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSw**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (8*cw**2*gPb**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gPb*gPw*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gPw**2*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSb**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gSb*gSw*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSw**2*MZ**4*sw**2)/Lambda**2))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.H,P.H):'(((gSh1**2*MH**4)/Lambda**2 + (2*gSh1*gSh2*MH**4)/Lambda**2 + (gSh2**2*MH**4)/Lambda**2 - (gSh1**2*MH**2*MY0**2)/Lambda**2 - (gSh1*gSh2*MH**2*MY0**2)/Lambda**2 + (gSh1**2*MY0**4)/(4.*Lambda**2))*cmath.sqrt(-4*MH**2*MY0**2 + MY0**4))/(32.*cmath.pi*abs(MY0)**3)',
                                   (P.t,P.t__tilde__):'((-12*gSu33**2*MT**2*yt**2 + 3*gPu33**2*MY0**2*yt**2 + 3*gSu33**2*MY0**2*yt**2)*cmath.sqrt(-4*MT**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.W__minus__,P.W__plus__):'(((48*gSw**2*MW**4)/Lambda**2 - (32*gPw**2*MW**2*MY0**2)/Lambda**2 - (32*gSw**2*MW**2*MY0**2)/Lambda**2 + (8*gPw**2*MY0**4)/Lambda**2 + (8*gSw**2*MY0**4)/Lambda**2 + (6*ee**2*gSh1*gSw*MW**2*vev**2)/(Lambda**2*sw**2) - (3*ee**2*gSh1*gSw*MY0**2*vev**2)/(Lambda**2*sw**2) + (3*ee**4*gSh1**2*vev**4)/(16.*Lambda**2*sw**4) - (ee**4*gSh1**2*MY0**2*vev**4)/(16.*Lambda**2*MW**2*sw**4) + (ee**4*gSh1**2*MY0**4*vev**4)/(64.*Lambda**2*MW**4*sw**4))*cmath.sqrt(-4*MW**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xc__tilde__,P.Xc):'(gSXc**2*MXc**2*cmath.sqrt(-4*MXc**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-8*gSXd**2*MXd**2 + 2*gPXd**2*MY0**2 + 2*gSXd**2*MY0**2)*cmath.sqrt(-4*MXd**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xr,P.Xr):'(gSXr**2*MXr**2*cmath.sqrt(-4*MXr**2*MY0**2 + MY0**4))/(32.*cmath.pi*abs(MY0)**3)',
                                   (P.Z,P.Z):'(((8*cw**4*gPw**2*MY0**4)/Lambda**2 + (8*cw**4*gSw**2*MY0**4)/Lambda**2 - (32*cw**4*gPw**2*MY0**2*MZ**2)/Lambda**2 - (32*cw**4*gSw**2*MY0**2*MZ**2)/Lambda**2 + (48*cw**4*gSw**2*MZ**4)/Lambda**2 + (16*cw**2*gPb*gPw*MY0**4*sw**2)/Lambda**2 + (16*cw**2*gSb*gSw*MY0**4*sw**2)/Lambda**2 - (64*cw**2*gPb*gPw*MY0**2*MZ**2*sw**2)/Lambda**2 - (64*cw**2*gSb*gSw*MY0**2*MZ**2*sw**2)/Lambda**2 + (96*cw**2*gSb*gSw*MZ**4*sw**2)/Lambda**2 + (8*gPb**2*MY0**4*sw**4)/Lambda**2 + (8*gSb**2*MY0**4*sw**4)/Lambda**2 - (32*gPb**2*MY0**2*MZ**2*sw**4)/Lambda**2 - (32*gSb**2*MY0**2*MZ**2*sw**4)/Lambda**2 + (48*gSb**2*MZ**4*sw**4)/Lambda**2 - (3*cw**2*ee**2*gSb*gSh1*MY0**2*vev**2)/Lambda**2 - (6*cw**2*ee**2*gSh1*gSw*MY0**2*vev**2)/Lambda**2 + (6*cw**2*ee**2*gSb*gSh1*MZ**2*vev**2)/Lambda**2 + (12*cw**2*ee**2*gSh1*gSw*MZ**2*vev**2)/Lambda**2 - (3*cw**4*ee**2*gSh1*gSw*MY0**2*vev**2)/(Lambda**2*sw**2) + (6*cw**4*ee**2*gSh1*gSw*MZ**2*vev**2)/(Lambda**2*sw**2) - (6*ee**2*gSb*gSh1*MY0**2*sw**2*vev**2)/Lambda**2 - (3*ee**2*gSh1*gSw*MY0**2*sw**2*vev**2)/Lambda**2 + (12*ee**2*gSb*gSh1*MZ**2*sw**2*vev**2)/Lambda**2 + (6*ee**2*gSh1*gSw*MZ**2*sw**2*vev**2)/Lambda**2 - (3*ee**2*gSb*gSh1*MY0**2*sw**4*vev**2)/(cw**2*Lambda**2) + (6*ee**2*gSb*gSh1*MZ**2*sw**4*vev**2)/(cw**2*Lambda**2) + (9*ee**4*gSh1**2*vev**4)/(8.*Lambda**2) + (3*ee**4*gSh1**2*MY0**4*vev**4)/(32.*Lambda**2*MZ**4) - (3*ee**4*gSh1**2*MY0**2*vev**4)/(8.*Lambda**2*MZ**2) + (3*cw**4*ee**4*gSh1**2*vev**4)/(16.*Lambda**2*sw**4) + (cw**4*ee**4*gSh1**2*MY0**4*vev**4)/(64.*Lambda**2*MZ**4*sw**4) - (cw**4*ee**4*gSh1**2*MY0**2*vev**4)/(16.*Lambda**2*MZ**2*sw**4) + (3*cw**2*ee**4*gSh1**2*vev**4)/(4.*Lambda**2*sw**2) + (cw**2*ee**4*gSh1**2*MY0**4*vev**4)/(16.*Lambda**2*MZ**4*sw**2) - (cw**2*ee**4*gSh1**2*MY0**2*vev**4)/(4.*Lambda**2*MZ**2*sw**2) + (3*ee**4*gSh1**2*sw**2*vev**4)/(4.*cw**2*Lambda**2) + (ee**4*gSh1**2*MY0**4*sw**2*vev**4)/(16.*cw**2*Lambda**2*MZ**4) - (ee**4*gSh1**2*MY0**2*sw**2*vev**4)/(4.*cw**2*Lambda**2*MZ**2) + (3*ee**4*gSh1**2*sw**4*vev**4)/(16.*cw**4*Lambda**2) + (ee**4*gSh1**2*MY0**4*sw**4*vev**4)/(64.*cw**4*Lambda**2*MZ**4) - (ee**4*gSh1**2*MY0**2*sw**4*vev**4)/(16.*cw**4*Lambda**2*MZ**2))*cmath.sqrt(MY0**4 - 4*MY0**2*MZ**2))/(32.*cmath.pi*abs(MY0)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.a,P.Y0):'((-MY0**2 + MZ**2)*((8*cw**2*gPb**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gPb*gPw*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gPw**2*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gSb**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gSb*gSw*MY0**4*sw**2)/Lambda**2 + (8*cw**2*gSw**2*MY0**4*sw**2)/Lambda**2 - (16*cw**2*gPb**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gPb*gPw*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gPw**2*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSb**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gSb*gSw*MY0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSw**2*MY0**2*MZ**2*sw**2)/Lambda**2 + (8*cw**2*gPb**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gPb*gPw*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gPw**2*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSb**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gSb*gSw*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSw**2*MZ**4*sw**2)/Lambda**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

