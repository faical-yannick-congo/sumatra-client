
class SimProject:

    def __init__(self, name, default_executable=None, default_script=None,
                 default_launch_mode=None, data_store='default'):
        self.name = name
        self.default_executable = default_executable
        self.default_script = default_script
        self.default_launch_mode = default_launch_mode
        self.record_groups = {}  # not sure how best to manage groups of simulations
        self.current_group = None
        self.data_store = data_store # a data store object
        self.last_record = None # not sure this is needed
        
        self._save()
        
    def _save(self):
        """Save state to some form of persistent storage. (file, database)."""
        pass
    
    def info(self):
        """Show some basic information about the project."""
        pass
    
    def launch_simulation(self, parameters, executable='default', script='default',
                          launch_mode='default', label=None, reason=None):
        """Launch a new simulation."""
        if executable == 'default':
            executable = self.default_executable
        if script == 'default':
            script = self.default_script
        if launch_mode == 'default':
            launch_mode = self.default_launch_mode
        sim_record = SimRecord(executable, script, parameters, launch_mode, label=label, reason=reason)
        self.add_record(sim_record)
        sim_record.run()
    
    def add_record(self, record):
        """Add a simulation record."""
        pass
    
    def get_record(self, label):
        """Search for a record with the supplied label and return it if found.
           Otherwise return None."""
        pass
    
    def delete_record(self, label):
        """Delete a record. Return 1 if the record is found.
           Otherwise return 0."""
        pass
        
    def delete_group(self, label):
        """Delete a group of records. Return the number of records deleted.
           Return 0 if the label is invalid."""
        pass
    
    