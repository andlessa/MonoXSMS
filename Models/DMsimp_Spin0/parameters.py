# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 14:17:57



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gSXr = Parameter(name = 'gSXr',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{SXr}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gSXc = Parameter(name = 'gSXc',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{SXc}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gSXd = Parameter(name = 'gSXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gPXd = Parameter(name = 'gPXd',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{PXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 4 ])

gSd11 = Parameter(name = 'gSd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 5 ])

gSu11 = Parameter(name = 'gSu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 6 ])

gSd22 = Parameter(name = 'gSd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 7 ])

gSu22 = Parameter(name = 'gSu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 8 ])

gSd33 = Parameter(name = 'gSd33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 9 ])

gSu33 = Parameter(name = 'gSu33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 10 ])

gPd11 = Parameter(name = 'gPd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gPu11 = Parameter(name = 'gPu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gPd22 = Parameter(name = 'gPd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gPu22 = Parameter(name = 'gPu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gPd33 = Parameter(name = 'gPd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gPu33 = Parameter(name = 'gPu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Pu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 10000.,
                   texname = '\\Lambda',
                   lhablock = 'DMINPUTS',
                   lhacode = [ 17 ])

gSg = Parameter(name = 'gSg',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Sg}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 18 ])

gPg = Parameter(name = 'gPg',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Pg}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 19 ])

gSh1 = Parameter(name = 'gSh1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Sh1}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 20 ])

gSh2 = Parameter(name = 'gSh2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{Sh2}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 21 ])

gSb = Parameter(name = 'gSb',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Sb}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 22 ])

gPb = Parameter(name = 'gPb',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Pb}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 23 ])

gSw = Parameter(name = 'gSw',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Sw}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 24 ])

gPw = Parameter(name = 'gPw',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Pw}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 25 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 51 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MY0 = Parameter(name = 'MY0',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY0}',
                lhablock = 'MASS',
                lhacode = [ 54 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WY0 = Parameter(name = 'WY0',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY0}',
                lhablock = 'DECAY',
                lhacode = [ 54 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

