# Submitter: brizam(Martin del Campo, Briza)
# Partner  : devorek(DeVore, Kristen)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
  #  print()
    def show_listing(s):
        for l,t in enumerate(s.split('\n'), 1):
            print('{line: >4} {text}'.format(line = l, text = t.rstrip()))
    def is_legal_name(name):
        if name not in keyword.kwlist and re.match('([a-zA-Z]\w*)',name) and type(name) == str:
            return True
        else:
            return False
        
    def unique(iterable):
        iterated = []
        for i in iterable:
            if i not in iterated:
                iterated.append(i)
                yield i
        
    if type(type_name) != str:
        raise SyntaxError('Type of input is incorrect')
    
    if not is_legal_name(type_name):
        raise SyntaxError('Not a legal name')
   
    if type(field_names) not in [str,list]:
        raise SyntaxError('Type of input is incorrect')
    else: 
        if type(field_names) == str:
            names = field_names.replace(',',' ')
            field_names = names.split()
        elif type(field_names) == list:
            pass

    field_names = [n for n in unique(field_names)]
    for name_item in field_names:
        if not is_legal_name(name_item):
            raise SyntaxError('Not a legal name')
        else:
            pass

    class_string = '''
class {type_name}:
    def __init__(self, {items}):
{extra_parameter}
    
        self._fields = {field_names}
        self._mutable = {mutable}
     
        
    def __repr__(self):
        return '{type_name}({inner_n})'.format({in_format})


    def __getitem__(self,index_value): 
        if type(index_value) == (str):
            if index_value in self._fields:
                return self.__dict__[index_value]
        
            else:
                raise IndexError('Index must be valid')
                
        elif type(index_value) == int:
            return (eval('self.get_'+self._fields[index_value]+'()'))
     
        else:
            raise IndexError('Index must be valid')


    def __eq__(self,value):
        if type(self) == type(value):
            if self._fields == value._fields:
                return self.__dict__ == value.__dict__
            else:
                return False
        else:
            return False

   
    def _replace(self,**kargs):
        if self._mutable:
            for k,v in kargs.items():
                if k in self._fields:
                    self.__dict__[k] = v                
                else:
                    raise TypeError('Attribute incorrect'+str(k))
            return None
                    
        else:
            for value in self._fields:
                if value not in kargs:
                    kargs[value] = self.__dict__[value]
                
            return {type_name}(**kargs)
        
    def __setattr__(self,name,value):
        if '_mutable' not in self.__dict__:
            self.__dict__[name]=value
        elif self._mutable:
            self.__dict__[name]=value
        else:
            raise AttributeError(str(name)+'Can not be changed or added')
        
        
        
        '''

    new_variable = ''
    
    new_str = ', '
    items_two = ', '.join(field_names)
    for field in field_names:
        new_variable += '        self.' + field + ' =' + ' ' + field + '\n'
   
    def for_repr_inner(names): 
        inner_format = ''   
        for name in names:
            inner_format += (name+'='+'{'+name+'}'+',')
        return inner_format[:-1]
    
    def for_repr_inside_format(names):
        in_format=''
        for name in names:
            in_format += (name+'='+'self.'+name+',')
        return in_format[:-1]
    
    
    
    class_definition = class_string.format(type_name = type_name, 
                                           field_names=field_names, 
                                           items = items_two, 
                                           mutable = mutable, 
                                           extra_parameter = new_variable,
                                           inner_n = for_repr_inner(field_names),
                                           in_format = for_repr_inside_format(field_names))
                                         
    get_function_string = '''
    def get_{single_item}(self):
        return self.{single_item}
    '''
    def get_funct_definition(names):
        get_str = ''
        for name in names:
            get_str += (get_function_string.format(single_item = name)) 
        return get_str
    
    class_definition +=  get_funct_definition(field_names)
  
    
    
 #   print(class_definition)
   # print(class_definition)
         
    # put your code here

    # bind class_definition (used below) to the string constructed for the class



    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace; then, bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__='pnamedtuple_{type}'.format(type = type_name))
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except(TypeError, SyntaxError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
   # pnamedtuple('Triple1', 'a b c',mutable=False)
    # Test pnamedtuple below: e.g., Point = pnamedtuple('Point', 'x y')

    import driver
    driver.driver()
